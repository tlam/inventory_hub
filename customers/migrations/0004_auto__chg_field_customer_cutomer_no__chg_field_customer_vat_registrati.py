# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Customer.cutomer_no'
        db.alter_column('customers_customer', 'cutomer_no', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Customer.vat_registration_number'
        db.alter_column('customers_customer', 'vat_registration_number', self.gf('django.db.models.fields.IntegerField')(blank=True))

        # Changing field 'Customer.business_registration_number'
        db.alter_column('customers_customer', 'business_registration_number', self.gf('django.db.models.fields.CharField')(max_length=9, blank=True))

        # Changing field 'Customer.discount_percent'
        db.alter_column('customers_customer', 'discount_percent', self.gf('django.db.models.fields.FloatField')(blank=True))

        # Changing field 'Customer.email'
        db.alter_column('customers_customer', 'email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True))


    def backwards(self, orm):
        
        # Changing field 'Customer.cutomer_no'
        db.alter_column('customers_customer', 'cutomer_no', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True))

        # Changing field 'Customer.vat_registration_number'
        db.alter_column('customers_customer', 'vat_registration_number', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Customer.business_registration_number'
        db.alter_column('customers_customer', 'business_registration_number', self.gf('django.db.models.fields.CharField')(max_length=9))

        # Changing field 'Customer.discount_percent'
        db.alter_column('customers_customer', 'discount_percent', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Customer.email'
        db.alter_column('customers_customer', 'email', self.gf('django.db.models.fields.CharField')(max_length=100))


    models = {
        'customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'business_registration_number': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.City']"}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Country']"}),
            'cutomer_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'discount_percent': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'vat_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'vat_registration_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'geography.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'geography.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['customers']
