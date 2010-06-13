# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Customer'
        db.create_table('customers_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cutomer_no', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('price_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.City'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.Country'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('vat_flag', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('vat_registration_number', self.gf('django.db.models.fields.IntegerField')()),
            ('business_registration_number', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('discount_percent', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('customers', ['Customer'])

        # Adding M2M table for field phone on 'Customer'
        db.create_table('customers_customer_phone', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('customer', models.ForeignKey(orm['customers.customer'], null=False)),
            ('phone', models.ForeignKey(orm['communications.phone'], null=False))
        ))
        db.create_unique('customers_customer_phone', ['customer_id', 'phone_id'])


    def backwards(self, orm):
        
        # Deleting model 'Customer'
        db.delete_table('customers_customer')

        # Removing M2M table for field phone on 'Customer'
        db.delete_table('customers_customer_phone')


    models = {
        'communications.phone': {
            'Meta': {'object_name': 'Phone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'business_registration_number': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.City']"}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Country']"}),
            'cutomer_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'discount_percent': ('django.db.models.fields.FloatField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['communications.Phone']", 'symmetrical': 'False'}),
            'price_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'vat_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'vat_registration_number': ('django.db.models.fields.IntegerField', [], {})
        },
        'geography.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'geography.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['customers']
