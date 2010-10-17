# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'LocalSupplier.town'
        db.add_column('suppliers_localsupplier', 'town', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.Town'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'LocalSupplier.town'
        db.delete_column('suppliers_localsupplier', 'town_id')


    models = {
        'geography.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'geography.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'geography.town': {
            'Meta': {'ordering': "['name']", 'object_name': 'Town'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'suppliers.foreignsupplier': {
            'Meta': {'object_name': 'ForeignSupplier'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.City']"}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Country']"}),
            'creditors_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'price_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'supplier_no': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'suppliers.localsupplier': {
            'Meta': {'object_name': 'LocalSupplier'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'business_registration_number': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.City']"}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Country']"}),
            'creditors_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'price_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'supplier_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'town': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Town']", 'null': 'True', 'blank': 'True'}),
            'vat_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vat_registration_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['suppliers']
