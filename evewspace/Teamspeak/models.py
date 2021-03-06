#    Eve W-Space
#    Copyright (C) 2013  Andrew Austin and other contributors
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version. An additional term under section
#    7 of the GPL is included in the LICENSE file.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.

class TeamspeakServer(models.Model):
    """Stores teamspeak server configuration."""
    host = models.CharField(max_length=100)
    queryuser = models.CharField(max_length=100)
    querypass = models.CharField(max_length=100)
    queryport = models.IntegerField()
    voiceport = models.IntegerField()
    # If enforcegroups = True, any TS users who do not have a GroupMap entry will have no groups
    enforcegroups = models.BooleanField()
    # If enforceusers = True, any TS users without a Django user mapping will be removed
    enforeceusers = models.BooleanField()

class GroupMap(models.Model):
    """Maps Django user groups to Teamspeak groups."""
    tsserver = models.ForeignKey(TeamspeakServer, related_name="groupmaps")
    usergroup = models.ForeignKey(Group, related_name="teamspeakgroups")
    tsgroup = models.CharField(max_length=100)

