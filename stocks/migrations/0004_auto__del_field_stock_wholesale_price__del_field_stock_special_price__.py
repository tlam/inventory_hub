# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Stock.wholesale_price'
        db.delete_column('stocks_stock', 'wholesale_price_id')

        # Deleting field 'Stock.special_price'
        db.delete_column('stocks_stock', 'special_price_id')

        # Deleting field 'Stock.retail_price'
        db.delete_column('stocks_stock', 'retail_price_id')

        # Deleting field 'Stock.dealer_price'
        db.delete_column('stocks_stock', 'dealer_price_id')


    def backwards(self, orm):
        
        # Adding field 'Stock.wholesale_price'
        db.add_column('stocks_stock', 'wholesale_price', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='wholesale', to=orm['stocks.Price']), keep_default=False)

        # Adding field 'Stock.special_price'
        db.add_column('stocks_stock', 'special_price', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='special', to=orm['stocks.Price']), keep_default=False)

        # Adding field 'Stock.retail_price'
        db.add_column('stocks_stock', 'retail_price', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='retail', to=orm['stocks.Price']), keep_default=False)

        # Adding field 'Stock.dealer_price'
        db.add_column('stocks_stock', 'dealer_price', self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='dealer', to=orm['stocks.Price']), keep_default=False)


    models = {
        'stocks.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
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
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'exempt_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'nonstock_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'pieces_per_box': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['stocks']
