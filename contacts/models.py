import re

from django.db import models

from customers.models import Customer


class ContactList(models.Model):
    description = models.CharField(max_length=10, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.description


    def email_filter(self, name):
        if name.startswith('email-input'):
            return name

    def phone_filter(self, name):
        if name.startswith('phone-input'):
            return name

    def get_dict(self):
        contacts = {}
        i = 0
        for contact in self.contacts.all():
            contacts[i] = {
                'first_name': contact.first_name,
                'last_name': contact.last_name,
                'pk': contact.pk,
                'emails': [],
                'phones': [],
            }
            for phone in contact.phones.all():
                contacts[i]['phones'].append(phone.get_dict())
            for email in contact.emails.all():
                contacts[i]['emails'].append(email.get_dict())
            i += 1
        return contacts

    @staticmethod
    def post_dict(data):
        keys = data.keys()
        keys.sort()

        contact_index = data.getlist('contact-index')
        contact_index = [int(x) for x in contact_index]
        contacts = {}
        for i in contact_index:
            def email_filter(name): return name.startswith('email-input-%i' % i)
            email_keys = filter(email_filter, keys)

            def phone_filter(name): return name.startswith('phone-input-%i' % i)
            phone_keys = filter(phone_filter, keys)

            contacts[i] = {
                'first_name': data.get('first-name-%i' % i),
                'last_name': data.get('last-name-%i' % i),
                'pk': int(data.get('contact-pk-%i' % i)),
            }

            email_list = []
            for email in email_keys:
                j = int(re.search('\d+$', email).group())
                email_list.append({
                    'address': data.get(email),
                    'email_type': data.get('email-type-%i-%i' % (i, j)),
                    'pk': int(data.get('email-pk-%i-%i' % (i, j))),
                })
            contacts[i].update({'emails': email_list})

            phone_list = []
            for phone in phone_keys:
                j = int(re.search('\d+$', phone).group())
                phone_list.append({
                    'number': data.get(phone),
                    'phone_type': data.get('phone-type-%i-%i' % (i, j)),
                    'pk': int(data.get('phone-pk-%i-%i' % (i, j))),
                })
            contacts[i].update({'phones': phone_list})
        return contacts

    def update_contacts(self, contacts):
        for i, contact in contacts.items():
            first_name = contact.get('first_name', '')
            last_name = contact.get('last_name', '')
            emails = contact.get('emails', [])
            phones = contact.get('phones', [])

            if not first_name and not last_name:
                return 'Please enter both a first and last name'

            if contact.get('pk', 0):
                updated_contact = Contact.objects.get(pk=contact['pk'])
                updated_contact.first_name = first_name
                updated_contact.last_name = last_name
                updated_contact.save()
            else:
                updated_contact = Contact.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    contact_list=self,
                )

            emails_msg = updated_contact.update_emails(emails)
            if emails_msg:
                return emails_msg

            phones_msg = updated_contact.update_phones(phones)
            if phones_msg:
                return phones_msg

        return ''


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_list = models.ForeignKey(ContactList, related_name='contacts')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def update_emails(self, emails):
        for email in emails:
            address = email.get('address', '')
            email_type = email.get('email_type', '')
            if not address:
                return 'Please enter an email address'
            if email.get('pk', 0):
                updated_email = Email.objects.get(pk=email['pk'])
                updated_email.address = address
                updated_email.email_type = email_type
                updated_email.save()
            else:
                Email.objects.create(
                    contact=self,
                    address=address,
                    email_type=email_type,
                )

    def update_phones(self, phones):
        for phone in phones:
            number = phone.get('number', '')
            phone_type = phone.get('phone_type', '')
            if not number:
                return 'Please enter a phone number'
            if phone.get('pk', 0):
                updated_phone = Phone.objects.get(pk=phone['pk'])
                updated_phone.number = number
                updated_phone.phone_type = phone_type
                updated_phone.save()
            else:
                Phone.objects.create(
                    contact=self,
                    number=number,
                    phone_type=phone_type,
                )


class Email(models.Model):
    EMAIL_CHOICES = (
        (u'H', u'Home'),
        (u'W', u'Work'),
    )
    contact = models.ForeignKey(Contact, blank=True, null=True, related_name='emails')
    address = models.EmailField()
    email_type = models.CharField(max_length=1, choices=EMAIL_CHOICES)

    def get_dict(self):
        return {
            'address': self.address,
            'email_type': self.email_type,
            'pk': self.pk,
        }

class Phone(models.Model):
    PHONE_CHOICES = (
        (u'H', u'Home'),
        (u'HF', u'Home Fax'),
        (u'W', u'Work'),
        (u'WF', u'Work Fax'),
        (u'C', u'Cellphone'),
    )
    contact = models.ForeignKey(Contact, blank=True, null=True, related_name='phones')
    number = models.CharField(max_length=50)
    phone_type = models.CharField(max_length=2, choices=PHONE_CHOICES)

    def get_dict(self):
        return {
            'number': self.number,
            'phone_type': self.phone_type,
            'pk': self.pk,
        }

