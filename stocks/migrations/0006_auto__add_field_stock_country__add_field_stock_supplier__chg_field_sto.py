# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Stock.country'
        db.add_column('stocks_stock', 'country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.Country'], null=True), keep_default=False)

        # Adding field 'Stock.supplier'
        db.add_column('stocks_stock', 'supplier', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['suppliers.Supplier'], null=True), keep_default=False)

        # Changing field 'Stock.retail_unit'
        db.alter_column('stocks_stock', 'retail_unit', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True))

        # Changing field 'Stock.dealer_unit'
        db.alter_column('stocks_stock', 'dealer_unit', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True))

        # Changing field 'Stock.special_unit'
        db.alter_column('stocks_stock', 'special_unit', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True))

        # Changing field 'Stock.wholesale_unit'
        db.alter_column('stocks_stock', 'wholesale_unit', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True))

        # Adding unique constraint on 'Category', fields ['name']
        db.create_unique('stocks_category', ['name'])

        # Adding unique constraint on 'Warehouse', fields ['name']
        db.create_unique('stocks_warehouse', ['name'])


    def backwards(self, orm):
        
        # Deleting field 'Stock.country'
        db.delete_column('stocks_stock', 'country_id')

        # Deleting field 'Stock.supplier'
        db.delete_column('stocks_stock', 'supplier_id')

        # Changing field 'Stock.retail_unit'
        db.alter_column('stocks_stock', 'retail_unit', self.gf('django.db.models.fields.CharField')(max_length=2))

        # Changing field 'Stock.dealer_unit'
        db.alter_column('stocks_stock', 'dealer_unit', self.gf('django.db.models.fields.CharField')(max_length=2))

        # Changing field 'Stock.special_unit'
        db.alter_column('stocks_stock', 'special_unit', self.gf('django.db.models.fields.CharField')(max_length=2))

        # Changing field 'Stock.wholesale_unit'
        db.alter_column('stocks_stock', 'wholesale_unit', self.gf('django.db.models.fields.CharField')(max_length=2))

        # Removing unique constraint on 'Category', fields ['name']
        db.delete_unique('stocks_category', ['name'])

        # Removing unique constraint on 'Warehouse', fields ['name']
        db.delete_unique('stocks_warehouse', ['name'])


    models = {
        'communications.phone': {
            'Meta': {'object_name': 'Phone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': '2'})
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
        },
        'stocks.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'})
        },
        'stocks.price': {
            'Meta': {'object_name': 'Price'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measurement': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'})
        },
        'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Category']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Country']", 'null': 'True'}),
            'dealer_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'dealer_unit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'exempt_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'nonstock_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'pieces_per_box': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'retail_unit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2', 'blank': 'True'}),
            'special_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'special_unit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['suppliers.Supplier']", 'null': 'True'}),
            'wholesale_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'wholesale_unit': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2', 'blank': 'True'})
        },
        'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'})
        },
        'suppliers.supplier': {
            'Meta': {'object_name': 'Supplier'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'business_registration_number': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.City']"}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Country']"}),
            'creditors_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'phone': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['communications.Phone']", 'null': 'True', 'symmetrical': 'False'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'price_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'supplier_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'vat_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'vat_registration_number': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['stocks']
