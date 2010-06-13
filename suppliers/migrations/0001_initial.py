# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Supplier'
        db.create_table('suppliers_supplier', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('supplier_no', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('company_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('creditors_code', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('price_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.City'])),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['geography.Country'])),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=6, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('vat_flag', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('vat_registration_number', self.gf('django.db.models.fields.IntegerField')()),
            ('business_registration_number', self.gf('django.db.models.fields.CharField')(max_length=9)),
        ))
        db.send_create_signal('suppliers', ['Supplier'])

        # Adding M2M table for field phone on 'Supplier'
        db.create_table('suppliers_supplier_phone', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('supplier', models.ForeignKey(orm['suppliers.supplier'], null=False)),
            ('phone', models.ForeignKey(orm['communications.phone'], null=False))
        ))
        db.create_unique('suppliers_supplier_phone', ['supplier_id', 'phone_id'])


    def backwards(self, orm):
        
        # Deleting model 'Supplier'
        db.delete_table('suppliers_supplier')

        # Removing M2M table for field phone on 'Supplier'
        db.delete_table('suppliers_supplier_phone')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'geography.country': {
            'Meta': {'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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

    complete_apps = ['suppliers']
