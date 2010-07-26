# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'CashSale'
        db.create_table('sales_cashsale', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invoice_no', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('quotation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quotations.Quotation'])),
            ('warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Warehouse'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.Customer'])),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('recquisition_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('discount', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal('sales', ['CashSale'])

        # Adding M2M table for field stocks on 'CashSale'
        db.create_table('sales_cashsale_stocks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cashsale', models.ForeignKey(orm['sales.cashsale'], null=False)),
            ('stock', models.ForeignKey(orm['stocks.stock'], null=False))
        ))
        db.create_unique('sales_cashsale_stocks', ['cashsale_id', 'stock_id'])

        # Adding model 'CreditSale'
        db.create_table('sales_creditsale', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invoice_no', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('quotation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quotations.Quotation'])),
            ('warehouse', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stocks.Warehouse'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.Customer'])),
            ('remarks', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('recquisition_number', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('discount', self.gf('django.db.models.fields.FloatField')(default=0)),
        ))
        db.send_create_signal('sales', ['CreditSale'])

        # Adding M2M table for field stocks on 'CreditSale'
        db.create_table('sales_creditsale_stocks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('creditsale', models.ForeignKey(orm['sales.creditsale'], null=False)),
            ('stock', models.ForeignKey(orm['stocks.stock'], null=False))
        ))
        db.create_unique('sales_creditsale_stocks', ['creditsale_id', 'stock_id'])


    def backwards(self, orm):
        
        # Deleting model 'CashSale'
        db.delete_table('sales_cashsale')

        # Removing M2M table for field stocks on 'CashSale'
        db.delete_table('sales_cashsale_stocks')

        # Deleting model 'CreditSale'
        db.delete_table('sales_creditsale')

        # Removing M2M table for field stocks on 'CreditSale'
        db.delete_table('sales_creditsale_stocks')


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
            'discount': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_no': ('django.db.models.fields.IntegerField', [], {}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'stocks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['stocks.Stock']", 'symmetrical': 'False'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Warehouse']"})
        },
        'sales.cashsale': {
            'Meta': {'object_name': 'CashSale'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customers.Customer']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'discount': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_no': ('django.db.models.fields.IntegerField', [], {}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quotation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quotations.Quotation']"}),
            'recquisition_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'stocks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['stocks.Stock']", 'symmetrical': 'False'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Warehouse']"})
        },
        'sales.creditsale': {
            'Meta': {'object_name': 'CreditSale'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customers.Customer']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'discount': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice_no': ('django.db.models.fields.IntegerField', [], {}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'quotation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['quotations.Quotation']"}),
            'recquisition_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'stocks': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['stocks.Stock']", 'symmetrical': 'False'}),
            'warehouse': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Warehouse']"})
        },
        'stocks.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'})
        },
        'stocks.stock': {
            'Meta': {'object_name': 'Stock'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['stocks.Category']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Country']", 'null': 'True', 'blank': 'True'}),
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
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['suppliers.Supplier']", 'null': 'True', 'blank': 'True'}),
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
            'vat_flag': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'vat_registration_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        }
    }

    complete_apps = ['sales']