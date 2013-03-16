# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Paste'
        db.create_table(u'pastebin_paste', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('syntax', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=30)),
            ('poster', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
        ))
        db.send_create_signal(u'pastebin', ['Paste'])


    def backwards(self, orm):
        # Deleting model 'Paste'
        db.delete_table(u'pastebin_paste')


    models = {
        u'pastebin.paste': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'Paste'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'syntax': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '30'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['pastebin']