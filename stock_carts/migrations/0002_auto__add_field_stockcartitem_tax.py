# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'StockCartItem.tax'
        db.add_column('stock_carts_stockcartitem', 'tax', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=4, decimal_places=2), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'StockCartItem.tax'
        db.delete_column('stock_carts_stockcartitem', 'tax')


    models = {
        'geography.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'stock_carts.stockcart': {
            'Meta': {'object_name': 'StockCart'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'stock_carts.stockcartitem': {
            'Meta': {'object_name': 'StockCartItem'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stock_carts.StockCart']"}),
            'discount': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'stock': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Stock']"}),
            'tax': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '4', 'decimal_places': '2'})
        },
        'stocks.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'})
        },
        'stocks.colour': {
            'Meta': {'object_name': 'Colour'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'caliber': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Category']"}),
            'colour': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Colour']", 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Country']", 'null': 'True', 'blank': 'True'}),
            'dealer_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'dealer_unit': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '2'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'exempt_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'item_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'nonstock_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pieces_per_box': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'retail_unit': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '2'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'special_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'special_unit': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '2'}),
            'tonality': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'}),
            'wholesale_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'}),
            'wholesale_unit': ('django.db.models.fields.CharField', [], {'default': "'U'", 'max_length': '2'})
        }
    }

    complete_apps = ['stock_carts']
