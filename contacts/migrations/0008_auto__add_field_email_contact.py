# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Email.contact'
        db.add_column('contacts_email', 'contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Email.contact'
        db.delete_column('contacts_email', 'contact_id')


    models = {
        'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'contact_list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': "orm['contacts.ContactList']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'contacts.contactlist': {
            'Meta': {'object_name': 'ContactList'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contacts.email': {
            'Meta': {'object_name': 'Email'},
            'address': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Contact']", 'null': 'True', 'blank': 'True'}),
            'email_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contacts.phone': {
            'Meta': {'object_name': 'Phone'},
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.Contact']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        }
    }

    complete_apps = ['contacts']
