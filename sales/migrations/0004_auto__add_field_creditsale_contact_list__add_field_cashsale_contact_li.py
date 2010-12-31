# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'CreditSale.contact_list'
        db.add_column('sales_creditsale', 'contact_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.ContactList'], null=True, blank=True), keep_default=False)

        # Adding field 'CashSale.contact_list'
        db.add_column('sales_cashsale', 'contact_list', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.ContactList'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'CreditSale.contact_list'
        db.delete_column('sales_creditsale', 'contact_list_id')

        # Deleting field 'CashSale.contact_list'
        db.delete_column('sales_cashsale', 'contact_list_id')


    models = {
        'contacts.contactlist': {
            'Meta': {'object_name': 'ContactList'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'customers.customer': {
            'Meta': {'unique_together': "(('first_name', 'last_name'),)", 'object_name': 'Customer'},
            'business_registration_number': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.City']", 'null': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'contact_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.ContactList']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Country']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 12, 30, 15, 38, 32, 988630)', 'auto_now_add': 'True', 'blank': 'True'}),
            'customer_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'discount_percent': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_company': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price_type': ('django.db.models.fields.CharField', [], {'default': "'R'", 'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'unit_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 12, 30, 15, 38, 32, 988630)', 'auto_now': 'True', 'blank': 'True'}),
            'vat_registration_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
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
        'sales.cashsale': {
            'Meta': {'object_name': 'CashSale'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock_carts.StockCart']", 'null': 'True', 'blank': 'True'}),
            'contact_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.ContactList']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 12, 30, 15, 38, 33, 46800)', 'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customers.Customer']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_no': ('django.db.models.fields.IntegerField', [], {}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'requisition_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 12, 30, 15, 38, 33, 46883)', 'auto_now': 'True', 'blank': 'True'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['warehouses.Warehouse']"})
        },
        'sales.creditsale': {
            'Meta': {'object_name': 'CreditSale'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock_carts.StockCart']", 'null': 'True', 'blank': 'True'}),
            'contact_list': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contacts.ContactList']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 12, 30, 15, 38, 33, 46800)', 'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customers.Customer']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_no': ('django.db.models.fields.IntegerField', [], {}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'requisition_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 12, 30, 15, 38, 33, 46883)', 'auto_now': 'True', 'blank': 'True'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['warehouses.Warehouse']"})
        },
        'stock_carts.stockcart': {
            'Meta': {'object_name': 'StockCart'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'warehouses.warehouse': {
            'Meta': {'ordering': "['name']", 'object_name': 'Warehouse'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['sales']
