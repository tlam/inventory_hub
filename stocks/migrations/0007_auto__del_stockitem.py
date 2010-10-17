# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'StockItem'
        db.delete_table('stocks_stockitem')


    def backwards(self, orm):
        
        # Adding model 'StockItem'
        db.create_table('stocks_stockitem', (
            ('discount', self.gf('django.db.models.fields.FloatField')(default=0, blank=True)),
            ('cash_sale', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cash_sale', null=True, to=orm['sales.CashSale'], blank=True)),
            ('stock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Stock'])),
            ('credit_sale', self.gf('django.db.models.fields.related.ForeignKey')(related_name='credit_sale', null=True, to=orm['sales.CreditSale'], blank=True)),
            ('quotation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quotations.Quotation'], null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
        ))
        db.send_create_signal('stocks', ['StockItem'])


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
        'stocks.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'})
        },
        'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Category']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Country']", 'null': 'True', 'blank': 'True'}),
            'dealer_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'dealer_unit': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '2'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'exempt_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'foreign_supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['suppliers.ForeignSupplier']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'local_supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['suppliers.LocalSupplier']", 'null': 'True', 'blank': 'True'}),
            'nonstock_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pieces_per_box': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'retail_unit': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '2'}),
            'special_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'special_unit': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '2'}),
            'wholesale_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'wholesale_unit': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '2'})
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
            'vat_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vat_registration_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['stocks']
