# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'CreditSale.discount'
        db.delete_column('sales_creditsale', 'discount')

        # Deleting field 'CreditSale.quantity'
        db.delete_column('sales_creditsale', 'quantity')

        # Removing M2M table for field stocks on 'CreditSale'
        db.delete_table('sales_creditsale_stocks')

        # Deleting field 'CashSale.discount'
        db.delete_column('sales_cashsale', 'discount')

        # Deleting field 'CashSale.quantity'
        db.delete_column('sales_cashsale', 'quantity')

        # Removing M2M table for field stocks on 'CashSale'
        db.delete_table('sales_cashsale_stocks')


    def backwards(self, orm):
        
        # Adding field 'CreditSale.discount'
        db.add_column('sales_creditsale', 'discount', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'CreditSale.quantity'
        db.add_column('sales_creditsale', 'quantity', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding M2M table for field stocks on 'CreditSale'
        db.create_table('sales_creditsale_stocks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('creditsale', models.ForeignKey(orm['sales.creditsale'], null=False)),
            ('stock', models.ForeignKey(orm['stocks.stock'], null=False))
        ))
        db.create_unique('sales_creditsale_stocks', ['creditsale_id', 'stock_id'])

        # Adding field 'CashSale.discount'
        db.add_column('sales_cashsale', 'discount', self.gf('django.db.models.fields.FloatField')(default=0), keep_default=False)

        # Adding field 'CashSale.quantity'
        db.add_column('sales_cashsale', 'quantity', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding M2M table for field stocks on 'CashSale'
        db.create_table('sales_cashsale_stocks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cashsale', models.ForeignKey(orm['sales.cashsale'], null=False)),
            ('stock', models.ForeignKey(orm['stocks.stock'], null=False))
        ))
        db.create_unique('sales_cashsale_stocks', ['cashsale_id', 'stock_id'])


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
        },
        'quotations.quotation': {
            'Meta': {'object_name': 'Quotation'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customers.Customer']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_no': ('django.db.models.fields.IntegerField', [], {}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Warehouse']"})
        },
        'sales.cashsale': {
            'Meta': {'object_name': 'CashSale'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customers.Customer']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_no': ('django.db.models.fields.IntegerField', [], {}),
            'quotation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quotations.Quotation']"}),
            'recquisition_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Warehouse']"})
        },
        'sales.creditsale': {
            'Meta': {'object_name': 'CreditSale'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customers.Customer']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_no': ('django.db.models.fields.IntegerField', [], {}),
            'quotation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quotations.Quotation']"}),
            'recquisition_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Warehouse']"})
        },
        'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['sales']
