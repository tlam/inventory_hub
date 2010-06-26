# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Quotation.discount'
        db.delete_column('quotations_quotation', 'discount')

        # Deleting field 'Quotation.quantity'
        db.delete_column('quotations_quotation', 'quantity')

        # Removing M2M table for field stocks on 'Quotation'
        db.delete_table('quotations_quotation_stocks')


    def backwards(self, orm):
        
        # Adding field 'Quotation.discount'
        db.add_column('quotations_quotation', 'discount', self.gf('django.db.models.fields.FloatField')(default=0, blank=True), keep_default=False)

        # Adding field 'Quotation.quantity'
        db.add_column('quotations_quotation', 'quantity', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True), keep_default=False)

        # Adding M2M table for field stocks on 'Quotation'
        db.create_table('quotations_quotation_stocks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quotation', models.ForeignKey(orm['quotations.quotation'], null=False)),
            ('stock', models.ForeignKey(orm['stocks.stock'], null=False))
        ))
        db.create_unique('quotations_quotation_stocks', ['quotation_id', 'stock_id'])


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
        'stocks.warehouse': {
            'Meta': {'object_name': 'Warehouse'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['quotations']
