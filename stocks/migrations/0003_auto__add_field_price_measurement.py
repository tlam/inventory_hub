# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Price.measurement'
        db.add_column('stocks_price', 'measurement', self.gf('django.db.models.fields.CharField')(default='', max_length=2), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Price.measurement'
        db.delete_column('stocks_price', 'measurement')


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
            'dealer_price': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dealer'", 'to': "orm['stocks.Price']"}),
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'exempt_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_code': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'nonstock_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'pieces_per_box': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'retail_price': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'retail'", 'to': "orm['stocks.Price']"}),
            'special_price': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'special'", 'to': "orm['stocks.Price']"}),
            'wholesale_price': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wholesale'", 'to': "orm['stocks.Price']"})
        },
        'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['stocks']
