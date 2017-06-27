# -*- coding: utf-8 -*-
#BEGIN_HEADER

# from biokbase.workspace.client import Workspace
from Workspace.WorkspaceClient import Workspace

from SetAPI.reads.ReadsSetInterfaceV1 import ReadsSetInterfaceV1
from SetAPI.assembly.AssemblySetInterfaceV1 import AssemblySetInterfaceV1
from SetAPI.genome.GenomeSetInterfaceV1 import GenomeSetInterfaceV1
from SetAPI.readsalignment.ReadsAlignmentSetInterfaceV1 import ReadsAlignmentSetInterfaceV1
from SetAPI.featureset.FeatureSetSetInterfaceV1 import FeatureSetSetInterfaceV1
from SetAPI.generic.GenericSetNavigator import GenericSetNavigator
from SetAPI.generic.DynamicServiceCache import DynamicServiceCache


#END_HEADER


class SetAPI:
    '''
    Module Name:
    SetAPI

    Module Description:

    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.1.3"
    GIT_URL = "https://github.com/briehl/SetAPI"
    GIT_COMMIT_HASH = "aba4ebe2ff67a1c087ad7b534e4162bbc6e5eb19"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        self.serviceWizardURL = config['service-wizard']
        self.dataPaletteServiceVersion = config['datapaletteservice-version']
        self.dataPaletteCache = DynamicServiceCache(self.serviceWizardURL,
                                                      self.dataPaletteServiceVersion,
                                                      'DataPaletteService')
        #END_CONSTRUCTOR
        pass


    def get_featureset_set_v1(self, ctx, params):
        """
        :param params: instance of type "GetFeatureSetSetV1Params" (ref -
           workspace reference to FeatureSetSet object. include_item_info - 1
           or 0, if 1 additionally provides workspace info (with metadata)
           for each FeatureSet object in the Set) -> structure: parameter
           "ref" of String, parameter "include_item_info" of type "boolean"
           (A boolean. 0 = false, 1 = true.), parameter "ref_path_to_set" of
           list of String
        :returns: instance of type "GetFeatureSetSetV1Result" -> structure:
           parameter "data" of type "FeatureSetSet" (When building a
           FeatureSetSet, all FeatureSets must be aligned against the same
           genome. This is not part of the object type, but enforced during a
           call to save_featureset_set_v1. @meta ws description as
           description @meta ws length(items) as item_count) -> structure:
           parameter "description" of String, parameter "items" of list of
           type "FeatureSetSetItem" (When saving a FeatureSetSet, only 'ref'
           is required. You should never set 'info'.  'info' is provided
           optionally when fetching the FeatureSetSet.) -> structure:
           parameter "ref" of type "ws_featureset_id" (The workspace id for a
           ReadsAlignment data object. @id ws KBaseCollections.FeatureSet),
           parameter "label" of String, parameter "info" of type
           "object_info" (Information about an object, including user
           provided metadata. obj_id objid - the numerical id of the object.
           obj_name name - the name of the object. type_string type - the
           type of the object. timestamp save_date - the save date of the
           object. obj_ver ver - the version of the object. username saved_by
           - the user that saved or copied the object. ws_id wsid - the
           workspace containing the object. ws_name workspace - the workspace
           containing the object. string chsum - the md5 checksum of the
           object. int size - the size of the object in bytes. usermeta meta
           - arbitrary user-supplied metadata about the object.) -> tuple of
           size 11: parameter "objid" of type "obj_id" (The unique, permanent
           numerical ID of an object.), parameter "name" of type "obj_name"
           (A string used as a name for an object. Any string consisting of
           alphanumeric characters and the characters |._- that is not an
           integer is acceptable.), parameter "type" of type "type_string" (A
           type string. Specifies the type and its version in a single string
           in the format [module].[typename]-[major].[minor]: module - a
           string. The module name of the typespec containing the type.
           typename - a string. The name of the type as assigned by the
           typedef statement. major - an integer. The major version of the
           type. A change in the major version implies the type has changed
           in a non-backwards compatible way. minor - an integer. The minor
           version of the type. A change in the minor version implies that
           the type has changed in a way that is backwards compatible with
           previous type definitions. In many cases, the major and minor
           versions are optional, and if not provided the most recent version
           will be used. Example: MyModule.MyType-3.1), parameter "save_date"
           of type "timestamp" (A time in the format YYYY-MM-DDThh:mm:ssZ,
           where Z is either the character Z (representing the UTC timezone)
           or the difference in time to UTC in the format +/-HHMM, eg:
           2012-12-17T23:24:06-0500 (EST time) 2013-04-03T08:56:32+0000 (UTC
           time) 2013-04-03T08:56:32Z (UTC time)), parameter "version" of
           Long, parameter "saved_by" of type "username" (Login name of a
           KBase user account.), parameter "wsid" of type "ws_id" (The
           unique, permanent numerical ID of a workspace.), parameter
           "workspace" of type "ws_name" (A string used as a name for a
           workspace. Any string consisting of alphanumeric characters and
           "_", ".", or "-" that is not an integer is acceptable. The name
           may optionally be prefixed with the workspace owner's user name
           and a colon, e.g. kbasetest:my_workspace.), parameter "chsum" of
           String, parameter "size" of Long, parameter "meta" of type
           "usermeta" (User provided metadata about an object. Arbitrary
           key-value pairs provided by the user.) -> mapping from String to
           String, parameter "info" of type "object_info" (Information about
           an object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_featureset_set_v1
        ws = Workspace(self.workspaceURL, token=ctx['token'])
        fssi = FeatureSetSetInterfaceV1(ws)
        result = fssi.get_featureset_set(ctx, params)
        #END get_featureset_set_v1

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method get_featureset_set_v1 return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [result]

    def save_featureset_set_v1(self, ctx, params):
        """
        :param params: instance of type "SaveFeatureSetSetV1Params"
           (workspace_name or workspace_id - alternative options defining
           target workspace, output_object_name - workspace object name (this
           parameter is used together with one of workspace params from
           above)) -> structure: parameter "workspace" of String, parameter
           "output_object_name" of String, parameter "data" of type
           "FeatureSetSet" (When building a FeatureSetSet, all FeatureSets
           must be aligned against the same genome. This is not part of the
           object type, but enforced during a call to save_featureset_set_v1.
           @meta ws description as description @meta ws length(items) as
           item_count) -> structure: parameter "description" of String,
           parameter "items" of list of type "FeatureSetSetItem" (When saving
           a FeatureSetSet, only 'ref' is required. You should never set
           'info'.  'info' is provided optionally when fetching the
           FeatureSetSet.) -> structure: parameter "ref" of type
           "ws_featureset_id" (The workspace id for a ReadsAlignment data
           object. @id ws KBaseCollections.FeatureSet), parameter "label" of
           String, parameter "info" of type "object_info" (Information about
           an object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String
        :returns: instance of type "SaveFeatureSetSetV1Result" -> structure:
           parameter "set_ref" of String, parameter "set_info" of type
           "object_info" (Information about an object, including user
           provided metadata. obj_id objid - the numerical id of the object.
           obj_name name - the name of the object. type_string type - the
           type of the object. timestamp save_date - the save date of the
           object. obj_ver ver - the version of the object. username saved_by
           - the user that saved or copied the object. ws_id wsid - the
           workspace containing the object. ws_name workspace - the workspace
           containing the object. string chsum - the md5 checksum of the
           object. int size - the size of the object in bytes. usermeta meta
           - arbitrary user-supplied metadata about the object.) -> tuple of
           size 11: parameter "objid" of type "obj_id" (The unique, permanent
           numerical ID of an object.), parameter "name" of type "obj_name"
           (A string used as a name for an object. Any string consisting of
           alphanumeric characters and the characters |._- that is not an
           integer is acceptable.), parameter "type" of type "type_string" (A
           type string. Specifies the type and its version in a single string
           in the format [module].[typename]-[major].[minor]: module - a
           string. The module name of the typespec containing the type.
           typename - a string. The name of the type as assigned by the
           typedef statement. major - an integer. The major version of the
           type. A change in the major version implies the type has changed
           in a non-backwards compatible way. minor - an integer. The minor
           version of the type. A change in the minor version implies that
           the type has changed in a way that is backwards compatible with
           previous type definitions. In many cases, the major and minor
           versions are optional, and if not provided the most recent version
           will be used. Example: MyModule.MyType-3.1), parameter "save_date"
           of type "timestamp" (A time in the format YYYY-MM-DDThh:mm:ssZ,
           where Z is either the character Z (representing the UTC timezone)
           or the difference in time to UTC in the format +/-HHMM, eg:
           2012-12-17T23:24:06-0500 (EST time) 2013-04-03T08:56:32+0000 (UTC
           time) 2013-04-03T08:56:32Z (UTC time)), parameter "version" of
           Long, parameter "saved_by" of type "username" (Login name of a
           KBase user account.), parameter "wsid" of type "ws_id" (The
           unique, permanent numerical ID of a workspace.), parameter
           "workspace" of type "ws_name" (A string used as a name for a
           workspace. Any string consisting of alphanumeric characters and
           "_", ".", or "-" that is not an integer is acceptable. The name
           may optionally be prefixed with the workspace owner's user name
           and a colon, e.g. kbasetest:my_workspace.), parameter "chsum" of
           String, parameter "size" of Long, parameter "meta" of type
           "usermeta" (User provided metadata about an object. Arbitrary
           key-value pairs provided by the user.) -> mapping from String to
           String
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN save_featureset_set_v1
        ws = Workspace(self.workspaceURL, token=ctx['token'])
        fssi = FeatureSetSetInterfaceV1(ws)
        result = fssi.save_featureset_set(ctx, params)
        #END save_featureset_set_v1

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method save_featureset_set_v1 return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def get_reads_alignment_set_v1(self, ctx, params):
        """
        :param params: instance of type "GetReadsAlignmentSetV1Params" (ref -
           workspace reference to ReadsAlignmentSet object. include_item_info
           - 1 or 0, if 1 additionally provides workspace info (with
           metadata) for each ReadsAlignment object in the Set) -> structure:
           parameter "ref" of String, parameter "include_item_info" of type
           "boolean" (A boolean. 0 = false, 1 = true.), parameter
           "ref_path_to_set" of list of String
        :returns: instance of type "GetReadsAlignmentSetV1Result" ->
           structure: parameter "data" of type "ReadsAlignmentSet" (When
           building a ReadsAlignmentSet, all ReadsAlignments must be aligned
           against the same genome. This is not part of the object type, but
           enforced during a call to save_reads_alignment_v1. @meta ws
           description as description @meta ws length(items) as item_count)
           -> structure: parameter "description" of String, parameter "items"
           of list of type "ReadsAlignmentSetItem" (When saving a
           ReadsAlignmentSet, only 'ref' is required. You should never set
           'info'.  'info' is provided optionally when fetching the
           ReadsAlignmentSet.) -> structure: parameter "ref" of type
           "ws_reads_align_id" (The workspace id for a ReadsAlignment data
           object. @id ws KBaseRNASeq.RNASeqAlignment), parameter "label" of
           String, parameter "info" of type "object_info" (Information about
           an object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String, parameter "info" of
           type "object_info" (Information about an object, including user
           provided metadata. obj_id objid - the numerical id of the object.
           obj_name name - the name of the object. type_string type - the
           type of the object. timestamp save_date - the save date of the
           object. obj_ver ver - the version of the object. username saved_by
           - the user that saved or copied the object. ws_id wsid - the
           workspace containing the object. ws_name workspace - the workspace
           containing the object. string chsum - the md5 checksum of the
           object. int size - the size of the object in bytes. usermeta meta
           - arbitrary user-supplied metadata about the object.) -> tuple of
           size 11: parameter "objid" of type "obj_id" (The unique, permanent
           numerical ID of an object.), parameter "name" of type "obj_name"
           (A string used as a name for an object. Any string consisting of
           alphanumeric characters and the characters |._- that is not an
           integer is acceptable.), parameter "type" of type "type_string" (A
           type string. Specifies the type and its version in a single string
           in the format [module].[typename]-[major].[minor]: module - a
           string. The module name of the typespec containing the type.
           typename - a string. The name of the type as assigned by the
           typedef statement. major - an integer. The major version of the
           type. A change in the major version implies the type has changed
           in a non-backwards compatible way. minor - an integer. The minor
           version of the type. A change in the minor version implies that
           the type has changed in a way that is backwards compatible with
           previous type definitions. In many cases, the major and minor
           versions are optional, and if not provided the most recent version
           will be used. Example: MyModule.MyType-3.1), parameter "save_date"
           of type "timestamp" (A time in the format YYYY-MM-DDThh:mm:ssZ,
           where Z is either the character Z (representing the UTC timezone)
           or the difference in time to UTC in the format +/-HHMM, eg:
           2012-12-17T23:24:06-0500 (EST time) 2013-04-03T08:56:32+0000 (UTC
           time) 2013-04-03T08:56:32Z (UTC time)), parameter "version" of
           Long, parameter "saved_by" of type "username" (Login name of a
           KBase user account.), parameter "wsid" of type "ws_id" (The
           unique, permanent numerical ID of a workspace.), parameter
           "workspace" of type "ws_name" (A string used as a name for a
           workspace. Any string consisting of alphanumeric characters and
           "_", ".", or "-" that is not an integer is acceptable. The name
           may optionally be prefixed with the workspace owner's user name
           and a colon, e.g. kbasetest:my_workspace.), parameter "chsum" of
           String, parameter "size" of Long, parameter "meta" of type
           "usermeta" (User provided metadata about an object. Arbitrary
           key-value pairs provided by the user.) -> mapping from String to
           String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN get_reads_alignment_set_v1

        ws = Workspace(self.workspaceURL, token=ctx['token'])
        rasi = ReadsAlignmentSetInterfaceV1(ws)
        returnVal = rasi.get_reads_alignment_set(ctx, params)

        #END get_reads_alignment_set_v1

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method get_reads_alignment_set_v1 return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def save_reads_alignment_set_v1(self, ctx, params):
        """
        :param params: instance of type "SaveReadsAlignmentSetV1Params"
           (workspace_name or workspace_id - alternative options defining
           target workspace, output_object_name - workspace object name (this
           parameter is used together with one of workspace params from
           above)) -> structure: parameter "workspace" of String, parameter
           "output_object_name" of String, parameter "data" of type
           "ReadsAlignmentSet" (When building a ReadsAlignmentSet, all
           ReadsAlignments must be aligned against the same genome. This is
           not part of the object type, but enforced during a call to
           save_reads_alignment_v1. @meta ws description as description @meta
           ws length(items) as item_count) -> structure: parameter
           "description" of String, parameter "items" of list of type
           "ReadsAlignmentSetItem" (When saving a ReadsAlignmentSet, only
           'ref' is required. You should never set 'info'.  'info' is
           provided optionally when fetching the ReadsAlignmentSet.) ->
           structure: parameter "ref" of type "ws_reads_align_id" (The
           workspace id for a ReadsAlignment data object. @id ws
           KBaseRNASeq.RNASeqAlignment), parameter "label" of String,
           parameter "info" of type "object_info" (Information about an
           object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String
        :returns: instance of type "SaveReadsAlignmentSetV1Result" ->
           structure: parameter "set_ref" of String, parameter "set_info" of
           type "object_info" (Information about an object, including user
           provided metadata. obj_id objid - the numerical id of the object.
           obj_name name - the name of the object. type_string type - the
           type of the object. timestamp save_date - the save date of the
           object. obj_ver ver - the version of the object. username saved_by
           - the user that saved or copied the object. ws_id wsid - the
           workspace containing the object. ws_name workspace - the workspace
           containing the object. string chsum - the md5 checksum of the
           object. int size - the size of the object in bytes. usermeta meta
           - arbitrary user-supplied metadata about the object.) -> tuple of
           size 11: parameter "objid" of type "obj_id" (The unique, permanent
           numerical ID of an object.), parameter "name" of type "obj_name"
           (A string used as a name for an object. Any string consisting of
           alphanumeric characters and the characters |._- that is not an
           integer is acceptable.), parameter "type" of type "type_string" (A
           type string. Specifies the type and its version in a single string
           in the format [module].[typename]-[major].[minor]: module - a
           string. The module name of the typespec containing the type.
           typename - a string. The name of the type as assigned by the
           typedef statement. major - an integer. The major version of the
           type. A change in the major version implies the type has changed
           in a non-backwards compatible way. minor - an integer. The minor
           version of the type. A change in the minor version implies that
           the type has changed in a way that is backwards compatible with
           previous type definitions. In many cases, the major and minor
           versions are optional, and if not provided the most recent version
           will be used. Example: MyModule.MyType-3.1), parameter "save_date"
           of type "timestamp" (A time in the format YYYY-MM-DDThh:mm:ssZ,
           where Z is either the character Z (representing the UTC timezone)
           or the difference in time to UTC in the format +/-HHMM, eg:
           2012-12-17T23:24:06-0500 (EST time) 2013-04-03T08:56:32+0000 (UTC
           time) 2013-04-03T08:56:32Z (UTC time)), parameter "version" of
           Long, parameter "saved_by" of type "username" (Login name of a
           KBase user account.), parameter "wsid" of type "ws_id" (The
           unique, permanent numerical ID of a workspace.), parameter
           "workspace" of type "ws_name" (A string used as a name for a
           workspace. Any string consisting of alphanumeric characters and
           "_", ".", or "-" that is not an integer is acceptable. The name
           may optionally be prefixed with the workspace owner's user name
           and a colon, e.g. kbasetest:my_workspace.), parameter "chsum" of
           String, parameter "size" of Long, parameter "meta" of type
           "usermeta" (User provided metadata about an object. Arbitrary
           key-value pairs provided by the user.) -> mapping from String to
           String
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN save_reads_alignment_set_v1
        ws = Workspace(self.workspaceURL, token=ctx['token'])
        rasi = ReadsAlignmentSetInterfaceV1(ws)
        result = rasi.save_reads_alignment_set(ctx, params)
        #END save_reads_alignment_set_v1

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method save_reads_alignment_set_v1 return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def get_reads_set_v1(self, ctx, params):
        """
        :param params: instance of type "GetReadsSetV1Params" (ref -
           workspace reference to ReadsGroup object. include_item_info - 1 or
           0, if 1 additionally provides workspace info (with metadata) for
           each Reads object in the Set) -> structure: parameter "ref" of
           String, parameter "include_item_info" of type "boolean" (A
           boolean. 0 = false, 1 = true.), parameter "ref_path_to_set" of
           list of String
        :returns: instance of type "GetReadsSetV1Result" -> structure:
           parameter "data" of type "ReadsSet" (@meta ws description as
           description @meta ws length(items) as item_count) -> structure:
           parameter "description" of String, parameter "items" of list of
           type "ReadsSetItem" (When saving a ReadsSet, only 'ref' is
           required.  You should never set 'info'.  'info' is provided
           optionally when fetching the ReadsSet.) -> structure: parameter
           "ref" of type "ws_reads_id" (The workspace ID for a Reads data
           object. @id ws KBaseFile.PairedEndLibrary
           KBaseFile.SingleEndLibrary), parameter "label" of String,
           parameter "data_attachments" of list of type "DataAttachment" ->
           structure: parameter "name" of String, parameter "ref" of type
           "ws_obj_id" (The workspace ID for a any data object. @id ws),
           parameter "info" of type "object_info" (Information about an
           object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String, parameter "info" of
           type "object_info" (Information about an object, including user
           provided metadata. obj_id objid - the numerical id of the object.
           obj_name name - the name of the object. type_string type - the
           type of the object. timestamp save_date - the save date of the
           object. obj_ver ver - the version of the object. username saved_by
           - the user that saved or copied the object. ws_id wsid - the
           workspace containing the object. ws_name workspace - the workspace
           containing the object. string chsum - the md5 checksum of the
           object. int size - the size of the object in bytes. usermeta meta
           - arbitrary user-supplied metadata about the object.) -> tuple of
           size 11: parameter "objid" of type "obj_id" (The unique, permanent
           numerical ID of an object.), parameter "name" of type "obj_name"
           (A string used as a name for an object. Any string consisting of
           alphanumeric characters and the characters |._- that is not an
           integer is acceptable.), parameter "type" of type "type_string" (A
           type string. Specifies the type and its version in a single string
           in the format [module].[typename]-[major].[minor]: module - a
           string. The module name of the typespec containing the type.
           typename - a string. The name of the type as assigned by the
           typedef statement. major - an integer. The major version of the
           type. A change in the major version implies the type has changed
           in a non-backwards compatible way. minor - an integer. The minor
           version of the type. A change in the minor version implies that
           the type has changed in a way that is backwards compatible with
           previous type definitions. In many cases, the major and minor
           versions are optional, and if not provided the most recent version
           will be used. Example: MyModule.MyType-3.1), parameter "save_date"
           of type "timestamp" (A time in the format YYYY-MM-DDThh:mm:ssZ,
           where Z is either the character Z (representing the UTC timezone)
           or the difference in time to UTC in the format +/-HHMM, eg:
           2012-12-17T23:24:06-0500 (EST time) 2013-04-03T08:56:32+0000 (UTC
           time) 2013-04-03T08:56:32Z (UTC time)), parameter "version" of
           Long, parameter "saved_by" of type "username" (Login name of a
           KBase user account.), parameter "wsid" of type "ws_id" (The
           unique, permanent numerical ID of a workspace.), parameter
           "workspace" of type "ws_name" (A string used as a name for a
           workspace. Any string consisting of alphanumeric characters and
           "_", ".", or "-" that is not an integer is acceptable. The name
           may optionally be prefixed with the workspace owner's user name
           and a colon, e.g. kbasetest:my_workspace.), parameter "chsum" of
           String, parameter "size" of Long, parameter "meta" of type
           "usermeta" (User provided metadata about an object. Arbitrary
           key-value pairs provided by the user.) -> mapping from String to
           String
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN get_reads_set_v1

        ws = Workspace(self.workspaceURL, token=ctx['token'])
        rsi = ReadsSetInterfaceV1(ws)
        result = rsi.get_reads_set(ctx, params)

        #END get_reads_set_v1

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method get_reads_set_v1 return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def save_reads_set_v1(self, ctx, params):
        """
        :param params: instance of type "SaveReadsSetV1Params"
           (workspace_name or workspace_id - alternative options defining
           target workspace, output_object_name - workspace object name (this
           parameter is used together with one of workspace params from
           above)) -> structure: parameter "workspace" of String, parameter
           "output_object_name" of String, parameter "data" of type
           "ReadsSet" (@meta ws description as description @meta ws
           length(items) as item_count) -> structure: parameter "description"
           of String, parameter "items" of list of type "ReadsSetItem" (When
           saving a ReadsSet, only 'ref' is required.  You should never set
           'info'.  'info' is provided optionally when fetching the
           ReadsSet.) -> structure: parameter "ref" of type "ws_reads_id"
           (The workspace ID for a Reads data object. @id ws
           KBaseFile.PairedEndLibrary KBaseFile.SingleEndLibrary), parameter
           "label" of String, parameter "data_attachments" of list of type
           "DataAttachment" -> structure: parameter "name" of String,
           parameter "ref" of type "ws_obj_id" (The workspace ID for a any
           data object. @id ws), parameter "info" of type "object_info"
           (Information about an object, including user provided metadata.
           obj_id objid - the numerical id of the object. obj_name name - the
           name of the object. type_string type - the type of the object.
           timestamp save_date - the save date of the object. obj_ver ver -
           the version of the object. username saved_by - the user that saved
           or copied the object. ws_id wsid - the workspace containing the
           object. ws_name workspace - the workspace containing the object.
           string chsum - the md5 checksum of the object. int size - the size
           of the object in bytes. usermeta meta - arbitrary user-supplied
           metadata about the object.) -> tuple of size 11: parameter "objid"
           of type "obj_id" (The unique, permanent numerical ID of an
           object.), parameter "name" of type "obj_name" (A string used as a
           name for an object. Any string consisting of alphanumeric
           characters and the characters |._- that is not an integer is
           acceptable.), parameter "type" of type "type_string" (A type
           string. Specifies the type and its version in a single string in
           the format [module].[typename]-[major].[minor]: module - a string.
           The module name of the typespec containing the type. typename - a
           string. The name of the type as assigned by the typedef statement.
           major - an integer. The major version of the type. A change in the
           major version implies the type has changed in a non-backwards
           compatible way. minor - an integer. The minor version of the type.
           A change in the minor version implies that the type has changed in
           a way that is backwards compatible with previous type definitions.
           In many cases, the major and minor versions are optional, and if
           not provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String
        :returns: instance of type "SaveReadsSetV1Result" -> structure:
           parameter "set_ref" of String, parameter "set_info" of type
           "object_info" (Information about an object, including user
           provided metadata. obj_id objid - the numerical id of the object.
           obj_name name - the name of the object. type_string type - the
           type of the object. timestamp save_date - the save date of the
           object. obj_ver ver - the version of the object. username saved_by
           - the user that saved or copied the object. ws_id wsid - the
           workspace containing the object. ws_name workspace - the workspace
           containing the object. string chsum - the md5 checksum of the
           object. int size - the size of the object in bytes. usermeta meta
           - arbitrary user-supplied metadata about the object.) -> tuple of
           size 11: parameter "objid" of type "obj_id" (The unique, permanent
           numerical ID of an object.), parameter "name" of type "obj_name"
           (A string used as a name for an object. Any string consisting of
           alphanumeric characters and the characters |._- that is not an
           integer is acceptable.), parameter "type" of type "type_string" (A
           type string. Specifies the type and its version in a single string
           in the format [module].[typename]-[major].[minor]: module - a
           string. The module name of the typespec containing the type.
           typename - a string. The name of the type as assigned by the
           typedef statement. major - an integer. The major version of the
           type. A change in the major version implies the type has changed
           in a non-backwards compatible way. minor - an integer. The minor
           version of the type. A change in the minor version implies that
           the type has changed in a way that is backwards compatible with
           previous type definitions. In many cases, the major and minor
           versions are optional, and if not provided the most recent version
           will be used. Example: MyModule.MyType-3.1), parameter "save_date"
           of type "timestamp" (A time in the format YYYY-MM-DDThh:mm:ssZ,
           where Z is either the character Z (representing the UTC timezone)
           or the difference in time to UTC in the format +/-HHMM, eg:
           2012-12-17T23:24:06-0500 (EST time) 2013-04-03T08:56:32+0000 (UTC
           time) 2013-04-03T08:56:32Z (UTC time)), parameter "version" of
           Long, parameter "saved_by" of type "username" (Login name of a
           KBase user account.), parameter "wsid" of type "ws_id" (The
           unique, permanent numerical ID of a workspace.), parameter
           "workspace" of type "ws_name" (A string used as a name for a
           workspace. Any string consisting of alphanumeric characters and
           "_", ".", or "-" that is not an integer is acceptable. The name
           may optionally be prefixed with the workspace owner's user name
           and a colon, e.g. kbasetest:my_workspace.), parameter "chsum" of
           String, parameter "size" of Long, parameter "meta" of type
           "usermeta" (User provided metadata about an object. Arbitrary
           key-value pairs provided by the user.) -> mapping from String to
           String
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN save_reads_set_v1

        ws = Workspace(self.workspaceURL, token=ctx['token'])
        rsi = ReadsSetInterfaceV1(ws)
        result = rsi.save_reads_set(ctx, params)

        #END save_reads_set_v1

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method save_reads_set_v1 return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def get_assembly_set_v1(self, ctx, params):
        """
        :param params: instance of type "GetAssemblySetV1Params" (ref -
           workspace reference to AssemblyGroup object. include_item_info - 1
           or 0, if 1 additionally provides workspace info (with metadata)
           for each Assembly object in the Set) -> structure: parameter "ref"
           of String, parameter "include_item_info" of type "boolean" (A
           boolean. 0 = false, 1 = true.), parameter "ref_path_to_set" of
           list of String
        :returns: instance of type "GetAssemblySetV1Result" -> structure:
           parameter "data" of type "AssemblySet" (@meta ws description as
           description @meta ws length(items) as item_count) -> structure:
           parameter "description" of String, parameter "items" of list of
           type "AssemblySetItem" (When saving an AssemblySet, only 'ref' is
           required. You should never set 'info'.  'info' is provided
           optionally when fetching the AssemblySet.) -> structure: parameter
           "ref" of type "ws_assembly_id" (The workspace ID for an Assembly
           object. @id ws KBaseGenomeAnnotations.Assembly), parameter "label"
           of String, parameter "info" of type "object_info" (Information
           about an object, including user provided metadata. obj_id objid -
           the numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String, parameter "info" of
           type "object_info" (Information about an object, including user
           provided metadata. obj_id objid - the numerical id of the object.
           obj_name name - the name of the object. type_string type - the
           type of the object. timestamp save_date - the save date of the
           object. obj_ver ver - the version of the object. username saved_by
           - the user that saved or copied the object. ws_id wsid - the
           workspace containing the object. ws_name workspace - the workspace
           containing the object. string chsum - the md5 checksum of the
           object. int size - the size of the object in bytes. usermeta meta
           - arbitrary user-supplied metadata about the object.) -> tuple of
           size 11: parameter "objid" of type "obj_id" (The unique, permanent
           numerical ID of an object.), parameter "name" of type "obj_name"
           (A string used as a name for an object. Any string consisting of
           alphanumeric characters and the characters |._- that is not an
           integer is acceptable.), parameter "type" of type "type_string" (A
           type string. Specifies the type and its version in a single string
           in the format [module].[typename]-[major].[minor]: module - a
           string. The module name of the typespec containing the type.
           typename - a string. The name of the type as assigned by the
           typedef statement. major - an integer. The major version of the
           type. A change in the major version implies the type has changed
           in a non-backwards compatible way. minor - an integer. The minor
           version of the type. A change in the minor version implies that
           the type has changed in a way that is backwards compatible with
           previous type definitions. In many cases, the major and minor
           versions are optional, and if not provided the most recent version
           will be used. Example: MyModule.MyType-3.1), parameter "save_date"
           of type "timestamp" (A time in the format YYYY-MM-DDThh:mm:ssZ,
           where Z is either the character Z (representing the UTC timezone)
           or the difference in time to UTC in the format +/-HHMM, eg:
           2012-12-17T23:24:06-0500 (EST time) 2013-04-03T08:56:32+0000 (UTC
           time) 2013-04-03T08:56:32Z (UTC time)), parameter "version" of
           Long, parameter "saved_by" of type "username" (Login name of a
           KBase user account.), parameter "wsid" of type "ws_id" (The
           unique, permanent numerical ID of a workspace.), parameter
           "workspace" of type "ws_name" (A string used as a name for a
           workspace. Any string consisting of alphanumeric characters and
           "_", ".", or "-" that is not an integer is acceptable. The name
           may optionally be prefixed with the workspace owner's user name
           and a colon, e.g. kbasetest:my_workspace.), parameter "chsum" of
           String, parameter "size" of Long, parameter "meta" of type
           "usermeta" (User provided metadata about an object. Arbitrary
           key-value pairs provided by the user.) -> mapping from String to
           String
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN get_assembly_set_v1

        ws = Workspace(self.workspaceURL, token=ctx['token'])
        rsi = AssemblySetInterfaceV1(ws)
        result = rsi.get_assembly_set(ctx, params)

        #END get_assembly_set_v1

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method get_assembly_set_v1 return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def save_assembly_set_v1(self, ctx, params):
        """
        :param params: instance of type "SaveAssemblySetV1Params"
           (workspace_name or workspace_id - alternative options defining
           target workspace, output_object_name - workspace object name (this
           parameter is used together with one of workspace params from
           above)) -> structure: parameter "workspace" of String, parameter
           "output_object_name" of String, parameter "data" of type
           "AssemblySet" (@meta ws description as description @meta ws
           length(items) as item_count) -> structure: parameter "description"
           of String, parameter "items" of list of type "AssemblySetItem"
           (When saving an AssemblySet, only 'ref' is required. You should
           never set 'info'.  'info' is provided optionally when fetching the
           AssemblySet.) -> structure: parameter "ref" of type
           "ws_assembly_id" (The workspace ID for an Assembly object. @id ws
           KBaseGenomeAnnotations.Assembly), parameter "label" of String,
           parameter "info" of type "object_info" (Information about an
           object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String
        :returns: instance of type "SaveAssemblySetV1Result" -> structure:
           parameter "set_ref" of String, parameter "set_info" of type
           "object_info" (Information about an object, including user
           provided metadata. obj_id objid - the numerical id of the object.
           obj_name name - the name of the object. type_string type - the
           type of the object. timestamp save_date - the save date of the
           object. obj_ver ver - the version of the object. username saved_by
           - the user that saved or copied the object. ws_id wsid - the
           workspace containing the object. ws_name workspace - the workspace
           containing the object. string chsum - the md5 checksum of the
           object. int size - the size of the object in bytes. usermeta meta
           - arbitrary user-supplied metadata about the object.) -> tuple of
           size 11: parameter "objid" of type "obj_id" (The unique, permanent
           numerical ID of an object.), parameter "name" of type "obj_name"
           (A string used as a name for an object. Any string consisting of
           alphanumeric characters and the characters |._- that is not an
           integer is acceptable.), parameter "type" of type "type_string" (A
           type string. Specifies the type and its version in a single string
           in the format [module].[typename]-[major].[minor]: module - a
           string. The module name of the typespec containing the type.
           typename - a string. The name of the type as assigned by the
           typedef statement. major - an integer. The major version of the
           type. A change in the major version implies the type has changed
           in a non-backwards compatible way. minor - an integer. The minor
           version of the type. A change in the minor version implies that
           the type has changed in a way that is backwards compatible with
           previous type definitions. In many cases, the major and minor
           versions are optional, and if not provided the most recent version
           will be used. Example: MyModule.MyType-3.1), parameter "save_date"
           of type "timestamp" (A time in the format YYYY-MM-DDThh:mm:ssZ,
           where Z is either the character Z (representing the UTC timezone)
           or the difference in time to UTC in the format +/-HHMM, eg:
           2012-12-17T23:24:06-0500 (EST time) 2013-04-03T08:56:32+0000 (UTC
           time) 2013-04-03T08:56:32Z (UTC time)), parameter "version" of
           Long, parameter "saved_by" of type "username" (Login name of a
           KBase user account.), parameter "wsid" of type "ws_id" (The
           unique, permanent numerical ID of a workspace.), parameter
           "workspace" of type "ws_name" (A string used as a name for a
           workspace. Any string consisting of alphanumeric characters and
           "_", ".", or "-" that is not an integer is acceptable. The name
           may optionally be prefixed with the workspace owner's user name
           and a colon, e.g. kbasetest:my_workspace.), parameter "chsum" of
           String, parameter "size" of Long, parameter "meta" of type
           "usermeta" (User provided metadata about an object. Arbitrary
           key-value pairs provided by the user.) -> mapping from String to
           String
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN save_assembly_set_v1
        ws = Workspace(self.workspaceURL, token=ctx['token'])
        rsi = AssemblySetInterfaceV1(ws)
        result = rsi.save_assembly_set(ctx, params)


        #END save_assembly_set_v1

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method save_assembly_set_v1 return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def get_genome_set_v1(self, ctx, params):
        """
        :param params: instance of type "GetGenomeSetV1Params" (ref -
           workspace reference to GenomeGroup object. include_item_info - 1
           or 0, if 1 additionally provides workspace info (with metadata)
           for each Genome object in the Set) -> structure: parameter "ref"
           of String, parameter "include_item_info" of type "boolean" (A
           boolean. 0 = false, 1 = true.), parameter "ref_path_to_set" of
           list of String
        :returns: instance of type "GetGenomeSetV1Result" -> structure:
           parameter "data" of type "GenomeSet" (@meta ws description as
           description @meta ws length(items) as item_count) -> structure:
           parameter "description" of String, parameter "items" of list of
           type "GenomeSetItem" (When saving an GenomeSet, only 'ref' is
           required. You should never set 'info'.  'info' is provided
           optionally when fetching the GenomeSet.) -> structure: parameter
           "ref" of type "ws_genome_id" (The workspace ID for a Genome
           object. @id ws KBaseGenomes.Genome), parameter "label" of String,
           parameter "info" of type "object_info" (Information about an
           object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String, parameter "info" of
           type "object_info" (Information about an object, including user
           provided metadata. obj_id objid - the numerical id of the object.
           obj_name name - the name of the object. type_string type - the
           type of the object. timestamp save_date - the save date of the
           object. obj_ver ver - the version of the object. username saved_by
           - the user that saved or copied the object. ws_id wsid - the
           workspace containing the object. ws_name workspace - the workspace
           containing the object. string chsum - the md5 checksum of the
           object. int size - the size of the object in bytes. usermeta meta
           - arbitrary user-supplied metadata about the object.) -> tuple of
           size 11: parameter "objid" of type "obj_id" (The unique, permanent
           numerical ID of an object.), parameter "name" of type "obj_name"
           (A string used as a name for an object. Any string consisting of
           alphanumeric characters and the characters |._- that is not an
           integer is acceptable.), parameter "type" of type "type_string" (A
           type string. Specifies the type and its version in a single string
           in the format [module].[typename]-[major].[minor]: module - a
           string. The module name of the typespec containing the type.
           typename - a string. The name of the type as assigned by the
           typedef statement. major - an integer. The major version of the
           type. A change in the major version implies the type has changed
           in a non-backwards compatible way. minor - an integer. The minor
           version of the type. A change in the minor version implies that
           the type has changed in a way that is backwards compatible with
           previous type definitions. In many cases, the major and minor
           versions are optional, and if not provided the most recent version
           will be used. Example: MyModule.MyType-3.1), parameter "save_date"
           of type "timestamp" (A time in the format YYYY-MM-DDThh:mm:ssZ,
           where Z is either the character Z (representing the UTC timezone)
           or the difference in time to UTC in the format +/-HHMM, eg:
           2012-12-17T23:24:06-0500 (EST time) 2013-04-03T08:56:32+0000 (UTC
           time) 2013-04-03T08:56:32Z (UTC time)), parameter "version" of
           Long, parameter "saved_by" of type "username" (Login name of a
           KBase user account.), parameter "wsid" of type "ws_id" (The
           unique, permanent numerical ID of a workspace.), parameter
           "workspace" of type "ws_name" (A string used as a name for a
           workspace. Any string consisting of alphanumeric characters and
           "_", ".", or "-" that is not an integer is acceptable. The name
           may optionally be prefixed with the workspace owner's user name
           and a colon, e.g. kbasetest:my_workspace.), parameter "chsum" of
           String, parameter "size" of Long, parameter "meta" of type
           "usermeta" (User provided metadata about an object. Arbitrary
           key-value pairs provided by the user.) -> mapping from String to
           String
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN get_genome_set_v1
        ws = Workspace(self.workspaceURL, token=ctx['token'])
        rsi = GenomeSetInterfaceV1(ws)
        result = rsi.get_genome_set(ctx, params)
        #END get_genome_set_v1

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method get_genome_set_v1 return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def save_genome_set_v1(self, ctx, params):
        """
        :param params: instance of type "SaveGenomeSetV1Params"
           (workspace_name or workspace_id - alternative options defining
           target workspace, output_object_name - workspace object name (this
           parameter is used together with one of workspace params from
           above)) -> structure: parameter "workspace" of String, parameter
           "output_object_name" of String, parameter "data" of type
           "GenomeSet" (@meta ws description as description @meta ws
           length(items) as item_count) -> structure: parameter "description"
           of String, parameter "items" of list of type "GenomeSetItem" (When
           saving an GenomeSet, only 'ref' is required. You should never set
           'info'.  'info' is provided optionally when fetching the
           GenomeSet.) -> structure: parameter "ref" of type "ws_genome_id"
           (The workspace ID for a Genome object. @id ws
           KBaseGenomes.Genome), parameter "label" of String, parameter
           "info" of type "object_info" (Information about an object,
           including user provided metadata. obj_id objid - the numerical id
           of the object. obj_name name - the name of the object. type_string
           type - the type of the object. timestamp save_date - the save date
           of the object. obj_ver ver - the version of the object. username
           saved_by - the user that saved or copied the object. ws_id wsid -
           the workspace containing the object. ws_name workspace - the
           workspace containing the object. string chsum - the md5 checksum
           of the object. int size - the size of the object in bytes.
           usermeta meta - arbitrary user-supplied metadata about the
           object.) -> tuple of size 11: parameter "objid" of type "obj_id"
           (The unique, permanent numerical ID of an object.), parameter
           "name" of type "obj_name" (A string used as a name for an object.
           Any string consisting of alphanumeric characters and the
           characters |._- that is not an integer is acceptable.), parameter
           "type" of type "type_string" (A type string. Specifies the type
           and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String
        :returns: instance of type "SaveGenomeSetV1Result" -> structure:
           parameter "set_ref" of String, parameter "set_info" of type
           "object_info" (Information about an object, including user
           provided metadata. obj_id objid - the numerical id of the object.
           obj_name name - the name of the object. type_string type - the
           type of the object. timestamp save_date - the save date of the
           object. obj_ver ver - the version of the object. username saved_by
           - the user that saved or copied the object. ws_id wsid - the
           workspace containing the object. ws_name workspace - the workspace
           containing the object. string chsum - the md5 checksum of the
           object. int size - the size of the object in bytes. usermeta meta
           - arbitrary user-supplied metadata about the object.) -> tuple of
           size 11: parameter "objid" of type "obj_id" (The unique, permanent
           numerical ID of an object.), parameter "name" of type "obj_name"
           (A string used as a name for an object. Any string consisting of
           alphanumeric characters and the characters |._- that is not an
           integer is acceptable.), parameter "type" of type "type_string" (A
           type string. Specifies the type and its version in a single string
           in the format [module].[typename]-[major].[minor]: module - a
           string. The module name of the typespec containing the type.
           typename - a string. The name of the type as assigned by the
           typedef statement. major - an integer. The major version of the
           type. A change in the major version implies the type has changed
           in a non-backwards compatible way. minor - an integer. The minor
           version of the type. A change in the minor version implies that
           the type has changed in a way that is backwards compatible with
           previous type definitions. In many cases, the major and minor
           versions are optional, and if not provided the most recent version
           will be used. Example: MyModule.MyType-3.1), parameter "save_date"
           of type "timestamp" (A time in the format YYYY-MM-DDThh:mm:ssZ,
           where Z is either the character Z (representing the UTC timezone)
           or the difference in time to UTC in the format +/-HHMM, eg:
           2012-12-17T23:24:06-0500 (EST time) 2013-04-03T08:56:32+0000 (UTC
           time) 2013-04-03T08:56:32Z (UTC time)), parameter "version" of
           Long, parameter "saved_by" of type "username" (Login name of a
           KBase user account.), parameter "wsid" of type "ws_id" (The
           unique, permanent numerical ID of a workspace.), parameter
           "workspace" of type "ws_name" (A string used as a name for a
           workspace. Any string consisting of alphanumeric characters and
           "_", ".", or "-" that is not an integer is acceptable. The name
           may optionally be prefixed with the workspace owner's user name
           and a colon, e.g. kbasetest:my_workspace.), parameter "chsum" of
           String, parameter "size" of Long, parameter "meta" of type
           "usermeta" (User provided metadata about an object. Arbitrary
           key-value pairs provided by the user.) -> mapping from String to
           String
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN save_genome_set_v1
        ws = Workspace(self.workspaceURL, token=ctx['token'])
        rsi = GenomeSetInterfaceV1(ws)
        result = rsi.save_genome_set(ctx, params)
        #END save_genome_set_v1

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method save_genome_set_v1 return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def list_sets(self, ctx, params):
        """
        Use to get the top-level sets in a WS. Optionally can include
        one level down members of those sets.
        NOTE: DOES NOT PRESERVE ORDERING OF ITEM LIST IN DATA
        :param params: instance of type "ListSetParams" (workspace -
           workspace name or ID (alternative to workspaces parameter),
           workspaces - list of workspace name ot ID (alternative to
           workspace parameter), include_metadata - flag for including
           metadata into Set object info and into object info of items (it
           affects DP raw data as well), include_raw_data_palettes - advanced
           option designed for optimization of listing methods in
           NarrativeService.) -> structure: parameter "workspace" of String,
           parameter "workspaces" of String, parameter
           "include_set_item_info" of type "boolean" (A boolean. 0 = false, 1
           = true.), parameter "include_metadata" of type "boolean" (A
           boolean. 0 = false, 1 = true.), parameter
           "include_raw_data_palettes" of type "boolean" (A boolean. 0 =
           false, 1 = true.)
        :returns: instance of type "ListSetResult" (raw_data_palettes -
           optional DP output turned on by 'include_raw_data_palettes' in
           input parameters, raw_data_palette_refs - optional DP output
           (mapping from workspace Id to reference to DataPalette container
           existing in particular workspace) turned on by
           'include_raw_data_palettes' in input parameters,) -> structure:
           parameter "sets" of list of type "SetInfo" (dp_ref - optional
           reference to DataPalette container in case given set object is
           coming from DataPalette.) -> structure: parameter "ref" of type
           "ws_obj_id" (The workspace ID for a any data object. @id ws),
           parameter "info" of type "object_info" (Information about an
           object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String, parameter "items" of
           list of type "SetItemInfo" -> structure: parameter "ref" of type
           "ws_obj_id" (The workspace ID for a any data object. @id ws),
           parameter "info" of type "object_info" (Information about an
           object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String, parameter "dp_ref" of
           type "ws_obj_id" (The workspace ID for a any data object. @id ws),
           parameter "raw_data_palettes" of list of type "DataInfo" ->
           structure: parameter "ref" of type "ws_ref" (@id ws), parameter
           "info" of type "object_info" (Information about an object,
           including user provided metadata. obj_id objid - the numerical id
           of the object. obj_name name - the name of the object. type_string
           type - the type of the object. timestamp save_date - the save date
           of the object. obj_ver ver - the version of the object. username
           saved_by - the user that saved or copied the object. ws_id wsid -
           the workspace containing the object. ws_name workspace - the
           workspace containing the object. string chsum - the md5 checksum
           of the object. int size - the size of the object in bytes.
           usermeta meta - arbitrary user-supplied metadata about the
           object.) -> tuple of size 11: parameter "objid" of type "obj_id"
           (The unique, permanent numerical ID of an object.), parameter
           "name" of type "obj_name" (A string used as a name for an object.
           Any string consisting of alphanumeric characters and the
           characters |._- that is not an integer is acceptable.), parameter
           "type" of type "type_string" (A type string. Specifies the type
           and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String, parameter
           "raw_data_palette_refs" of mapping from String to String
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN list_sets

        ws = Workspace(self.workspaceURL, token=ctx['token'])
        gsn = GenericSetNavigator(ws, data_palette_cache=self.dataPaletteCache,
                                  token=ctx['token'])
        result = gsn.list_sets(params)

        #END list_sets

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method list_sets return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]

    def get_set_items(self, ctx, params):
        """
        Use to drill down into one or more sets, the position in the
        return 'sets' list will match the position in the input ref list.
        NOTE: DOES NOT PRESERVE ORDERING OF ITEM LIST IN DATA
        :param params: instance of type "GetSetItemsParams" -> structure:
           parameter "set_refs" of list of type "SetReference" -> structure:
           parameter "ref" of type "ws_obj_id" (The workspace ID for a any
           data object. @id ws), parameter "path_to_set" of list of type
           "ws_obj_id" (The workspace ID for a any data object. @id ws)
        :returns: instance of type "GetSetItemsResult" -> structure:
           parameter "sets" of list of type "SetInfo" (dp_ref - optional
           reference to DataPalette container in case given set object is
           coming from DataPalette.) -> structure: parameter "ref" of type
           "ws_obj_id" (The workspace ID for a any data object. @id ws),
           parameter "info" of type "object_info" (Information about an
           object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String, parameter "items" of
           list of type "SetItemInfo" -> structure: parameter "ref" of type
           "ws_obj_id" (The workspace ID for a any data object. @id ws),
           parameter "info" of type "object_info" (Information about an
           object, including user provided metadata. obj_id objid - the
           numerical id of the object. obj_name name - the name of the
           object. type_string type - the type of the object. timestamp
           save_date - the save date of the object. obj_ver ver - the version
           of the object. username saved_by - the user that saved or copied
           the object. ws_id wsid - the workspace containing the object.
           ws_name workspace - the workspace containing the object. string
           chsum - the md5 checksum of the object. int size - the size of the
           object in bytes. usermeta meta - arbitrary user-supplied metadata
           about the object.) -> tuple of size 11: parameter "objid" of type
           "obj_id" (The unique, permanent numerical ID of an object.),
           parameter "name" of type "obj_name" (A string used as a name for
           an object. Any string consisting of alphanumeric characters and
           the characters |._- that is not an integer is acceptable.),
           parameter "type" of type "type_string" (A type string. Specifies
           the type and its version in a single string in the format
           [module].[typename]-[major].[minor]: module - a string. The module
           name of the typespec containing the type. typename - a string. The
           name of the type as assigned by the typedef statement. major - an
           integer. The major version of the type. A change in the major
           version implies the type has changed in a non-backwards compatible
           way. minor - an integer. The minor version of the type. A change
           in the minor version implies that the type has changed in a way
           that is backwards compatible with previous type definitions. In
           many cases, the major and minor versions are optional, and if not
           provided the most recent version will be used. Example:
           MyModule.MyType-3.1), parameter "save_date" of type "timestamp" (A
           time in the format YYYY-MM-DDThh:mm:ssZ, where Z is either the
           character Z (representing the UTC timezone) or the difference in
           time to UTC in the format +/-HHMM, eg: 2012-12-17T23:24:06-0500
           (EST time) 2013-04-03T08:56:32+0000 (UTC time)
           2013-04-03T08:56:32Z (UTC time)), parameter "version" of Long,
           parameter "saved_by" of type "username" (Login name of a KBase
           user account.), parameter "wsid" of type "ws_id" (The unique,
           permanent numerical ID of a workspace.), parameter "workspace" of
           type "ws_name" (A string used as a name for a workspace. Any
           string consisting of alphanumeric characters and "_", ".", or "-"
           that is not an integer is acceptable. The name may optionally be
           prefixed with the workspace owner's user name and a colon, e.g.
           kbasetest:my_workspace.), parameter "chsum" of String, parameter
           "size" of Long, parameter "meta" of type "usermeta" (User provided
           metadata about an object. Arbitrary key-value pairs provided by
           the user.) -> mapping from String to String, parameter "dp_ref" of
           type "ws_obj_id" (The workspace ID for a any data object. @id ws)
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN get_set_items

        ws = Workspace(self.workspaceURL, token=ctx['token'])
        gsn = GenericSetNavigator(ws)
        result = gsn.get_set_items(params)

        #END get_set_items

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method get_set_items return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK", 'message': "", 'version': self.VERSION,
                     'git_url': self.GIT_URL, 'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
