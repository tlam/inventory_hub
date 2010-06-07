# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Category'
        db.create_table('stocks_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('stocks', ['Category'])

        # Adding model 'Warehouse'
        db.create_table('stocks_warehouse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
        ))
        db.send_create_signal('stocks', ['Warehouse'])

        # Adding model 'Price'
        db.create_table('stocks_price', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('retail_price', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=20, decimal_places=2)),
        ))
        db.send_create_signal('stocks', ['Price'])


    def backwards(self, orm):
        
        # Deleting model 'Category'
        db.delete_table('stocks_category')

        # Deleting model 'Warehouse'
        db.delete_table('stocks_warehouse')

        # Deleting model 'Price'
        db.delete_table('stocks_price')


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
            'retail_price': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '20', 'decimal_places': '2'})
        },
        'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['stocks']
