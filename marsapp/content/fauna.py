#-*- coding: utf-8 -*-
#  mars http://www.naturalsciences.be/metamars/products/
#  Archetypes implementation of the MARS core types based on ATContentTypes
#  Copyright (c) 2003-2007 MARS development team
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
"""

"""
__author__  = 'David Convent <david.convent@naturalsciences.be>'
__docformat__ = 'restructuredtext'


from api import *
from config import PROJECTNAME
from schemata import *

FaunaBiologySchema = BiologySchema.copy()
#FaunaBiologySchema['age'].vocabulary = fauna_age
FaunaBiologySchema['gender'].vocabulary = fauna_gender

FaunaBioRemainSchema = BioRemainSchema.copy()
FaunaBioRemainSchema['polarity'].vocabulary = fauna_polarity
FaunaBioRemainSchema['laterality'].vocabulary = fauna_laterality

FaunaBioAssemblageSchema = BioAssemblageSchema.copy()
FaunaBioAssemblageSchema['origin'].vocabulary = fauna_origin

FaunaPreservationSchema = PreservationSchema.copy()
FaunaPreservationSchema['preservation'].vocabulary = fauna_preservation

FaunaBurialSchema = BurialSchema.copy()
FaunaBurialSchema['burial'].vocabulary = fauna_burial


FaunaRemainSchema = MarsCollectionObjectSchema.copy()
FaunaRemainSchema += FaunaPreservationSchema
FaunaRemainSchema += CollectionObjectBaseSchema.copy()
FaunaRemainSchema += FaunaBioRemainSchema
FaunaRemainSchema += FaunaBiologySchema
FaunaRemainSchema += FaunaBurialSchema
FaunaRemainSchema += ChronologySchema.copy()
FaunaRemainSchema += ChronologyDatingSchema.copy()
FaunaRemainSchema += TaphonomySchema.copy()
FaunaRemainSchema += DiscoverySchema.copy()
FaunaRemainSchema += AdministrationSchema.copy()
FaunaRemainSchema['remainType'].widget.startup_directory = '/marscategories/remain-type/fauna'
finalizeMarsSchema(FaunaRemainSchema, delFields=['discoverySite'], remain_types=FAUNA_TYPES)

class MarsFaunaRemain(MarsCollectionObject):
    """Fauna Remain"""
    schema = FaunaRemainSchema

    portal_type = "Fauna Remain"
    archetype_name = "Fauna Remain"


FaunaIndividualSchema = MarsCollectionObjectSchema.copy()
FaunaIndividualSchema += FaunaPreservationSchema
FaunaIndividualSchema += CollectionObjectBaseSchema.copy()
FaunaIndividualSchema += BioIndividualSchema.copy()
FaunaIndividualSchema += FaunaBiologySchema
FaunaIndividualSchema += FaunaBurialSchema
FaunaIndividualSchema += ChronologySchema.copy()
FaunaIndividualSchema += ChronologyDatingSchema.copy()
FaunaIndividualSchema += TaphonomySchema.copy()
FaunaIndividualSchema += DiscoverySchema.copy()
FaunaIndividualSchema += AdministrationSchema.copy()
FaunaIndividualSchema['remainType'].widget.startup_directory = '/marscategories/remain-type/fauna'
finalizeMarsSchema(FaunaIndividualSchema, delFields=['discoverySite'], remain_types=FAUNA_TYPES)

class MarsFaunaIndividual(MarsCollectionObject):
    """Fauna Individual"""
    schema = FaunaIndividualSchema

    portal_type = "Fauna Individual"
    archetype_name = "Fauna Individual"


FaunaAssemblageSchema = MarsCollectionObjectSchema.copy()
FaunaAssemblageSchema += CollectionObjectBaseSchema.copy()
FaunaAssemblageSchema += AssemblageSchema.copy()
FaunaAssemblageSchema += FaunaBioAssemblageSchema
FaunaAssemblageSchema += FaunaBiologySchema
FaunaAssemblageSchema += FaunaBurialSchema
FaunaAssemblageSchema += ChronologySchema.copy()
FaunaAssemblageSchema += ChronologyDatingSchema.copy()
FaunaAssemblageSchema += TaphonomySchema.copy()
FaunaAssemblageSchema += DiscoverySchema.copy()
FaunaAssemblageSchema += AdministrationSchema.copy()
FaunaAssemblageSchema['remainType'].widget.startup_directory = '/marscategories/remain-type/fauna'
finalizeMarsSchema(FaunaAssemblageSchema, delFields=['discoverySite'], remain_types=FAUNA_TYPES, igNumbers=True)

class MarsFaunaAssemblage(MarsCollectionObject):
    """Fauna Assemblage"""
    schema = FaunaAssemblageSchema

    portal_type = "Fauna Assemblage"
    archetype_name = "Fauna Assemblage"


FaunaRefSampleSchema = MarsCollectionObjectSchema.copy()
FaunaRefSampleSchema += CollectionObjectBaseSchema.copy()
FaunaRefSampleSchema += RefSampleBonesSchema.copy()
FaunaRefSampleSchema += ChronologySchema.copy()
FaunaRefSampleSchema += AdministrationSchema.copy()
FaunaRefSampleSchema += AssemblageSchema.copy()
FaunaRefSampleSchema += FaunaBiologySchema
FaunaRefSampleSchema['remainType'].widget.startup_directory = '/marscategories/remain-type/fauna'
finalizeMarsSchema(FaunaRefSampleSchema, delFields=['discoverySite'], remain_types=FAUNA_TYPES, igNumbers=True)

class MarsFaunaReferenceSample(MarsCollectionObject):
    """Fauna Reference Sample"""
    schema = FaunaRefSampleSchema

    portal_type = "Fauna Reference Sample"
    archetype_name = "Fauna Reference Sample"


registerType(MarsFaunaRemain, PROJECTNAME)
registerType(MarsFaunaIndividual, PROJECTNAME)
registerType(MarsFaunaAssemblage, PROJECTNAME)
registerType(MarsFaunaReferenceSample, PROJECTNAME)
