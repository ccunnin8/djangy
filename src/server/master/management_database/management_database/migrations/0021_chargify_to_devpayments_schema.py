# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'User.subscription_id'
        db.delete_column('user', 'subscription_id')

        # Adding field 'User.first_name'
        db.add_column('user', 'first_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'User.last_name'
        db.add_column('user', 'last_name', self.gf('django.db.models.fields.CharField')(default=None, max_length=255, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'User.subscription_id'
        db.add_column('user', 'subscription_id', self.gf('django.db.models.fields.CharField')(default=-1, max_length=255), keep_default=False)

        # Deleting field 'User.first_name'
        db.delete_column('user', 'first_name')

        # Deleting field 'User.last_name'
        db.delete_column('user', 'last_name')


    models = {
        'management_database.allocationchange': {
            'Meta': {'object_name': 'AllocationChange', 'db_table': "'allocation_change'"},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['management_database.Application']"}),
            'billed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'component': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'management_database.application': {
            'Meta': {'object_name': 'Application', 'db_table': "'application'"},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['management_database.User']"}),
            'app_gid': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'bundle_version': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'cron_uid': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'db_host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'db_max_size_mb': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'db_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'db_password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'db_port': ('django.db.models.fields.IntegerField', [], {'default': '3306'}),
            'db_username': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'debug': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'num_procs': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'proc_mem_mb': ('django.db.models.fields.IntegerField', [], {'default': '64'}),
            'proc_num_threads': ('django.db.models.fields.IntegerField', [], {'default': '20'}),
            'proc_stack_mb': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'setup_uid': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'web_uid': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        },
        'management_database.collaborator': {
            'Meta': {'unique_together': "[('application', 'user')]", 'object_name': 'Collaborator', 'db_table': "'collaborator'"},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['management_database.Application']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['management_database.User']"})
        },
        'management_database.process': {
            'Meta': {'unique_together': "[('application', 'host'), ('host', 'port')]", 'object_name': 'Process', 'db_table': "'process'"},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['management_database.Application']"}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_procs': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'port': ('django.db.models.fields.IntegerField', [], {'default': '20000'})
        },
        'management_database.proxycache': {
            'Meta': {'object_name': 'ProxyCache', 'db_table': "'proxycache'"},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['management_database.Application']"}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'management_database.sshpublickey': {
            'Meta': {'object_name': 'SshPublicKey', 'db_table': "'ssh_public_key'"},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ssh_public_key': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['management_database.User']"})
        },
        'management_database.user': {
            'Meta': {'object_name': 'User', 'db_table': "'user'"},
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'customer_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_limit': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'passwd': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'referrer': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['management_database.User']", 'null': 'True', 'blank': 'True'})
        },
        'management_database.virtualhost': {
            'Meta': {'unique_together': "[('application', 'virtualhost')]", 'object_name': 'VirtualHost', 'db_table': "'virtualhost'"},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['management_database.Application']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'virtualhost': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'management_database.whitelist': {
            'Meta': {'object_name': 'WhiteList', 'db_table': "'whitelist'"},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invite_code': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'referrer': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['management_database.User']", 'null': 'True', 'blank': 'True'})
        },
        'management_database.workerhost': {
            'Meta': {'object_name': 'WorkerHost', 'db_table': "'worker_host'"},
            'host': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_procs': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        }
    }

    complete_apps = ['management_database']
