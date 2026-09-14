# Application

## Description

An Application is something that can be run by the user to generate or analyse simulation output.

## Standards

`PROV:Entity`. Note the potential confusion. An Application is something that has the potential to be an Activity (in the PROV sense) in the form of a Process. However, PROV only deals with the past, not with potential. The Application is a file somewhere, and hence an Entity.

## Automation

Most of this table is expected to be populated by the user.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_APPLICATION | Type | TEXT|
|  | Description | Unique key|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instatiating framework|
| PURPOSE | Type | TEXT|
|  | Description | Description of the purpose of the application|
|  | Standards | ?|
|  | Validation | Free text|
|  | Automation | None|
| VERSION | Type | TEXT|
|  | Description | Version ID for the application|
|  | Standards | dc:?|
|  | Validation | String (e.g. CHAR(32))|
|  | Automation | None|
| LICENCE | Type | TEXT|
|  | Description | Software licence for the application|
|  | Standards | dc:license|
|  | Validation | Free text with the option to select from other entries|
|  | Automation | None|
| LANGUAGE | Type | TEXT|
|  | Description | Programming language the application was written in|
|  | Standards | ?|
|  | Validation | Free text with the option to select from other entries|
|  | Automation | None|
| ENVS | Type | TEXT|
|  | Description | The environment variables that should be recorded when the application is run|
|  | Standards | None|
|  | Validation | List of strings|
|  | Automation | None|
| SEPARATOR | Type | TEXT|
|  | Description | Separator used when supplying arguments to the application|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| REVISION | Type | TEXT|
|  | Description | ID in Application table of Application this Application is a revision of, if any.|
|  | Standards | `PROV:wasDerivedFrom`; `dc:isVersionOF`|
|  | Validation | Must be an ID of an Application|
|  | Null | If not a revision of anoth Application.|
|  | Automation | None|
| MODEL | Type | TEXT|
|  | Description | ID in Model table of Model this application is, if it is a Model.|
|  | Standards | None|
|  | Validation | Must be an ID of a Model.|
|  | Null | If this Application is not a Model.|
|  | Automation | None|
| LOCATION | Type | TEXT|
|  | Description | ID in the Box table to use to find this application.|
|  | Standards | ?|
|  | Validation | Must be an ID of a Box.|
|  | Null | If the search for a Box for this Application has not been done.|
|  | Automation | This should be populated automatically the first time the Application is requested on a host by finding the most local Box that references it, and storing that here.

If the most local Box is not on the current host, then the Application should be downloaded to the current host, and a new Box created for the location.

If the Box ID is no longer present, then the search should be repeated in the Box table.
                  |

# Argument

## Description

A command-line argument accepted by an Application. Commands vary hugely in how they parse arguments on the command line, and this table needs to make clear how to build a command line that the Application can use. To be clear, a command line is a string of text that is given to a shell (DOS, bash, etc.) to initiate a batch job.

## Standards

POSIX.1-2008 and equivalently IEEE Std 1003.1-2008/Cor 1-2013 are normative for Unix environments, but cannot be assumed even for Unix environments. Cross-platform support is in any case needed.

## Automation

When building up a command-line for an Application with arguments during invocation of a Process, the system should do the following:
- Let M be a map from integer to list of string.
- For each flag, check with the user to see whether it should be set or cleared; if set, add the flag name to M, using the order as the key, or -1 if the order is null. Create an entry in ArgumentValue using ‘true’ or ‘false’ as the value according to whether or not the flag is set.
- For each option, check with the user to see whether it should be used, and if so, provide an appropriate argument or arguments in accordance with the arity. Build a string for the option including its name and arguments, bearing in mind the separator and argsep values. Add the resulting string to M.
- For each required argument, request a value or values from the user in accordance with the arity. Build a string accordingly and add to M.
- Let K be a sorted list of keys of M.
- Let C be a string.
- For each key, join its list of strings with space and concatenate to C.
- C contains the command-line argument string.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_ARGUMENT | Type | TEXT|
|  | Description | Unique key|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| TYPE | Type | TEXT|
|  | Description | The kind of command line argument this is. Required arguments must be provided, typically don’t have a name, and are identified by their number. Options typically have a name, which if given stipulates some sort of value must be provided. Flags are options with arity 0.|
|  | Standards | None|
|  | Validation | One of “required”, “option”, or “flag”|
|  | Automation | None|
| ORDER_VALUE | Type | INTEGER|
|  | Description | A number used to indicate any order in which this Argument should appear in relation to other Arguments the Application accepts.|
|  | Standards | None|
|  | Validation | Non-negative integer or null if the order is unimportant.|
|  | Automation | None|
| ASSIGNMENT_OPERATOR |  | |
|  | Type | TEXT|
|  | Description | Separator to use between argument name and value.|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|
| NAME | Type | TEXT|
|  | Description | The name of the argument, including any grammar to indicate on the command-line that it is an argument (such as –– or – or /).|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|
| SEPARATOR | Type | TEXT|
|  | Description | This is the character that indicates the argument name (e.g. --input, -input, /input).|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|
| SHORT_NAME | Type | TEXT|
|  | Description | The short name of the argument, including any grammar to indicate on the command-line that it is an argument (such as –– or – or /). For example in *nix system -h and --help are the same parameter.|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|
| SHORT_SEPARATOR |  | |
|  | Type | TEXT|
|  | Description | This is the character that indicates the argument name (e.g. --input, -input, /input). for example in *nix system -h and --help are the same parameter.|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|
| DESCRIPTION | Type | TEXT|
|  | Description | Short text to use to summarise what the argument is|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|
| ARITY | Type | TEXT|
|  | Description | Number of arguments expected. Can be integer, ?, + or *.|
|  | Standards | None|
|  | Validation | ?, + or *, or integer string. Constraints apply.|
|  | Automation | None|
| ARGSEP | Type | TEXT|
|  | Description | Separator to use between arguments if arity > 1|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|
| RANGE | Type | TEXT|
|  | Description | Description of the range of any value to be supplied by the user|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| APPLICATION | Type | TEXT|
|  | Description | The application this argument applies to.|
|  | Standards | None|
|  | Validation | ID in the Application table.|
|  | Null | Null if not an argument for an Application|
|  | Automation | None|
| VARIABLE | Type | TEXT|
|  | Description | The variable this argument relates to.|
|  | Standards | None|
|  | Validation | ID in the Variables table.|
|  | Null | Null if not about a variable|
|  | Automation | None|
| BOX_TYPE | Type | TEXT|
|  | Description | The BoxType this argument might be, if it is a file or somesuch.|
|  | Standards | None|
|  | Validation | ID in the BoxTypes table.|
|  | Null | Null if this does not have a BoxType associated iwth it.|
|  | Automation | None|

# ArgumentValue

## Description

A value supplied for a command-line argument in a run of an Application.

## Standards

None

## Automation

Populated automatically when a Process is invoked.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| HAS_VALUE | Type | TEXT|
|  | Description | Value supplied, or true/false for flags|
|  | Standards | None|
|  | Validation | None|
|  | Automation | Populated when the Process is invoked|
| FOR_PROCESS | Type | TEXT|
|  | Description | ID in Process table of the Process this ArgumentValue applies to|
|  | Standards | None|
|  | Validation | Must be an ID of a Process|
|  | Null | Not null|
|  | Automation | Populated automatically when the Process is created|
| FOR_ARGUMENT | Type | TEXT|
|  | Description | ID in Argument table of the Argument this value is for|
|  | Standards | None|
|  | Validation | Must be an ID of an Argument|
|  | Null | Not null|
|  | Automation | Populated automatically when the Process is created|
| BOX | Type | TEXT|
|  | Description | ID in Box table of the box this value can be for|
|  | Standards | None|
|  | Validation | Must be an ID of a Box|
|  | Null | Not null|
|  | Automation | Populated automatically when the Process is created|

# Assumes

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Standards

None

## Automation

This relationship may be inferred automatically from the use of StatisticalMethod or VisualisationMethod.

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| PERSON | Type | TEXT|
|  | Description | ID in Person table of the Person making the assumption|
|  | Standards | None|
|  | Validation | Must be an ID of a Person|
|  | Null | Not null|
|  | Automation | None|
| STATISTICS | Type | TEXT|
|  | Description | ID in Statistics table if assumption applies to a statistical computation|
|  | Standards | None|
|  | Validation | Must be an ID of a Statistics|
|  | Null | Null if Visualisation is not null|
|  | Automation | None|
| VISUALISATION | Type | TEXT|
|  | Description | ID in Visualisation table if assumption applies to a visualisation|
|  | Standards | None|
|  | Validation | Must be an ID of a Visualisation|
|  | Null | Null if Statistics is not null|
|  | Automation | None|
| VARIABLE | Type | TEXT|
|  | Description | ID in Variable table of the variable to which the assumption applies|
|  | Standards | None|
|  | Validation | Must be an ID of a Variable|
|  | Null | Not null|
|  | Automation | None|
| ASSUMPTION | Type | TEXT|
|  | Description | ID in Assumption table of the Assumption being made|
|  | Standards | None|
|  | Validation | Must be an ID of an Assumption|
|  | Null | Not null|
|  | Automation | None|

# Assumption

## Description

An Assumption is a condition applied to a Variable for its proper application to a Statistic. (That Statistic being realised as an Aggregation of the Variable to which the Assumption applies.) A Person makes an Assumption about a Variable (in the Assumes table), explicitly or implicitly, every time they compute the Statistic on it.

## Standards

None

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_ASSUMPTION | Type | TEXT|
|  | Description | Short name for the assumption|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | None|

# Box

## Description

A Box is any data container (file, database, URI, etc.) used to store or reference data within the system.

## Standards

`PROV:Entity`

## Automation

A Box should be created automatically whenever data is accessed or generated by a Process.
Metadata such as size, encoding, timestamps, and hash may be populated automatically using system tools (e.g. OS calls, HTTP headers, checksum utilities).


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_BOX | Type | TEXT|
|  | Description | Unique identifier for the Box|
|  | Standards | None|
|  | Validation | Primary key|
|  | Automation | Generated automatically|
| LOCATION_TYPE | Type | TEXT|
|  | Description | Type of resource the Box refers to (e.g. file, URI, database)|
|  | Standards | ?|
|  | Validation | String describing access type|
|  | Automation | Requires appropriate software depending on type|
| LOCATION_VALUE | Type | TEXT|
|  | Description | The means of accessing the resource (path, URI, connection string, etc.)|
|  | Standards | URI/IRI|
|  | Validation | Depends on LOCATION-TYPE|
|  | Automation | Parsed and used by system handlers|
| SIZE | Type | INTEGER|
|  | Description | Size of the resource in bytes|
|  | Standards | ISO/IEC 80000-13|
|  | Validation | Non-negative integer or null|
|  | Automation | Retrieved via OS or HTTP headers|
| ENCODING | Type | TEXT|
|  | Description | Encoding of the resource|
|  | Standards | MIME|
|  | Validation | Valid MIME type or null|
|  | Automation | Detected using system tools (e.g. file -I, HTTP headers)|
| CREATION_TIME | Type | TEXT|
|  | Description | Time the resource was created|
|  | Standards | ISO8601|
|  | Validation | Datetime string|
|  | Automation | Retrieved via OS stat or equivalent|
| MODIFICATION_TIME |  | |
|  | Type | TEXT|
|  | Description | Last modification time of the resource|
|  | Standards | ISO8601|
|  | Validation | Datetime string|
|  | Automation | Retrieved via OS stat or HTTP headers|
| UPDATE_TIME | Type | TEXT|
|  | Description | Time the metadata for this Box was last updated|
|  | Standards | ISO8601|
|  | Validation | Datetime string|
|  | Automation | System maintained|
| HASH | Type | TEXT|
|  | Description | Hash of the resource content|
|  | Standards | None|
|  | Validation | Format: algorithm:encoding:value|
|  | Automation | Generated using hashing tools (e.g. md5sum, sha256sum)|
| INSTANCE | Type | TEXT|
|  | Description | ID in BoxType table describing the type of Box|
|  | Standards | None|
|  | Validation | Must be an ID of a BoxType|
|  | Null | Not null|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| LOCATION_APPLICATION |  | |
|  | Type | TEXT|
|  | Description | ID in Application table if this Box refers to an Application|
|  | Standards | None|
|  | Validation | Must be an ID of an Application|
|  | Null | Null if not applicable|
|  | Automation | None|
| LOCATION_DOCUMENTATION |  | |
|  | Type | TEXT|
|  | Description | ID in Documentation table if this Box refers to Documentation|
|  | Standards | None|
|  | Validation | Must be an ID of Documentation|
|  | Null | Null if not applicable|
|  | Automation | None|
| GENERATED_BY | Type | TEXT|
|  | Description | ID in Study table of the Study that generated this Box|
|  | Standards | `PROV:wasGeneratedBy`|
|  | Validation | Must be an ID of a Study|
|  | Null | Null if not generated by a Study|
|  | Automation | Set when Process produces output|
| REPOSITORY_OF | Type | TEXT|
|  | Description | ID in Study table of Study this Box is a repository for|
|  | Standards | None|
|  | Validation | Must be an ID of a Study|
|  | Null | Optional|
|  | Automation | None|
| HELD_BY | Type | TEXT|
|  | Description | ID in Person table of person holding the Box|
|  | Standards | `PROV:wasAttributedTo`|
|  | Validation | Must be an ID of a Person|
|  | Null | Optional|
|  | Automation | None|
| SOURCED_FROM | Type | TEXT|
|  | Description | ID in Person table of source of the Box|
|  | Standards | `PROV:wasAttributedTo`|
|  | Validation | Must be an ID of a Person|
|  | Null | Optional|
|  | Automation | None|
| OUTPUT_OF | Type | TEXT|
|  | Description | ID in Process table of the Process that produced this Box|
|  | Standards | `PROV:wasGeneratedBy`|
|  | Validation | Must be an ID of a Process|
|  | Null | Null if not produced by a Process|
|  | Automation | Automatically set during Process execution|
| COLLECTION | Type | TEXT|
|  | Description | ID in Box table if this Box is part of another Box|
|  | Standards | PROV:hadMember|
|  | Validation | Must be an ID of a Box|
|  | Null | Null if not part of a collection|
|  | Automation | None|

# BoxType

## Description

A BoxType defines the format and identification rules for Boxes, describing how their contents should be interpreted.

## Standards

None

## Automation

BoxTypes are expected to be defined by the user; identification rules may be applied automatically when inspecting Box contents.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_BOX_TYPE | Type | TEXT|
|  | Description | Unique identifier for the BoxType|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| FORMAT | Type | TEXT|
|  | Description | Format of the Box contents|
|  | Standards | MIME|
|  | Validation | Valid MIME type|
|  | Automation | None|
| IDENTIFIER | Type | TEXT|
|  | Description | Rule used to identify whether a Box conforms to this BoxType (e.g. magic bytes, filename pattern)|
|  | Standards | None|
|  | Validation | Structured rule string|
|  | Automation | None|

# Computer

## Description

A Computer represents a machine on which Processes are executed.

## Standards

PROV:Agent

## Automation

Most values are expected to be automatically obtained from the operating system and network interfaces.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_COMPUTER | Type | TEXT|
|  | Description | Unique key|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| HOST_ID | Type | TEXT|
|  | Description | Identifier for the host machine|
|  | Standards | ?|
|  | Validation | String|
|  | Automation | Retrieved from the operating system|
| IP_ADDRESS | Type | TEXT|
|  | Description | IP address of the machine|
|  | Standards | ?|
|  | Validation | Valid IP address string|
|  | Automation | Retrieved from the network interface|
| MAC_ADDRESS | Type | TEXT|
|  | Description | MAC address of the machine|
|  | Standards | ?|
|  | Validation | Valid MAC address string|
|  | Automation | Retrieved from the network interface|

# Content

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The Content table describes how Variables (or StatisticalVariables) are located within a Box.

## Standards

None

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| OPTIONALITY | Type | TEXT|
|  | Description | Whether the Variable always appears or only appears depending on some condition|
|  | Standards | None|
|  | Validation | One of 'always' or 'depends'|
|  | Automation | None|
| LOCATOR | Type | TEXT|
|  | Description | How to locate the Variable's values within the Box (e.g. row:X, column:Y, field:Z)|
|  | Validation | Formatted rule string|
|  | Automation | None|
| TIME_LOCATOR | Type | TEXT|
|  | Description | How to locate the temporal context (e.g. timestamps)|
|  | Standards | None|
|  | Validation | Formatted rule string|
|  | Automation | None|
| LINK_LOCATOR | Type | TEXT|
|  | Description | How to locate link identifiers (for relational data)|
|  | Standards | None|
|  | Validation | Formatted rule string|
|  | Automation | None|
| AGENT_LOCATOR | Type | TEXT|
|  | Description | How to locate agent identifiers|
|  | Standards | None|
|  | Validation | Formatted rule string|
|  | Automation | None|
| STATISTICAL_VARIABLE |  | |
|  | Type | TEXT|
|  | Description | ID in StatisticalVariable table if this Content refers to a StatisticalVariable|
|  | Standards | None|
|  | Validation | Must be an ID of a StatisticalVariable|
|  | Null | Null if VARIABLE is not null|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| BOX_TYPE | Type | TEXT|
|  | Description | ID in BoxType table of the BoxType this Content applies to|
|  | Standards | None|
|  | Validation | Must be an ID of a BoxType|
|  | Null | Not null|
|  | Automation | None|
| VARIABLE | Type | TEXT|
|  | Description | ID in Variable table if this Content refers to a Variable|
|  | Standards | None|
|  | Validation | Must be an ID of a Variable|
|  | Null | Null if STATISTICAL_VARIABLE is not null|
|  | Automation | None|
| VISUALISATION_METHOD |  | |
|  | Type | TEXT|
|  | Description | ID in VisualisationMethod table if this Content is used for visualisation|
|  | Standards | None|
|  | Validation | Must be an ID of a VisualisationMethod|
|  | Null | Optional|
|  | Automation | None|

# Context

## Description

The Context table provides contextual values such as time, space, agent, or link, which can be associated with Values.

## Standards

None

## Automation

Context entries may be created automatically when extracting or interpreting data from Boxes.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_CONTEXT | Type | TEXT|
|  | Description | Unique identifier for the Context|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| VALUE | Type | TEXT|
|  | Description | Value of the context (e.g. time, space, agent, or link identifier)|
|  | Standards | None|
|  | Validation | String|
|  | Automation | Derived from Content locators or data extraction|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| PART | Type | TEXT|
|  | Description | ID in Context table indicating that this Context is part of another Context|
|  | Standards | None|
|  | Validation | Must be an ID of a Context|
|  | Null | Null if this Context is not part of another|
|  | Automation | None|

# Contributor

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The Contributor table records people who have contributed to Applications or Documentation, including how they are credited.

## Standards

dc:contributor

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| CONTRIBUTION | Type | TEXT|
|  | Description | Nature of the contribution made by the person|
|  | Standards | dc:contributor|
|  | Validation | String describing contribution type|
|  | Automation | None|
| ALIAS | Type | TEXT|
|  | Description | Name or alias used for the contributor in the context of the Application or Documentation|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| CONTRIBUTOR | Type | TEXT|
|  | Description | ID in Person table of the contributor|
|  | Standards | dc:contributor|
|  | Validation | Must be an ID of a Person|
|  | Null | Not null|
|  | Automation | None|
| DOCUMENTATION | Type | TEXT|
|  | Description | ID in Documentation table if the contribution relates to Documentation|
|  | Standards | dc:relation|
|  | Validation | Must be an ID of Documentation|
|  | Null | Null if APPLICATION is not null|
|  | Automation | None|
| APPLICATION | Type | TEXT|
|  | Description | ID in Application table if the contribution relates to an Application|
|  | Standards | dc:relation|
|  | Validation | Must be an ID of an Application|
|  | Null | Null if DOCUMENTATION is not null|
|  | Automation | None|

# Dependency

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The Dependency table records that one Application depends on another, optionally under certain conditions.

## Standards

None

## Automation

Dependencies may be inferred automatically in some cases, but are generally provided by the user.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| OPTIONALITY | Type | TEXT|
|  | Description | Whether the dependency is required, optional, or conditional|
|  | Standards | None|
|  | Validation | One of 'required', 'optional', or a condition string|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| DEPENDANT | Type | TEXT|
|  | Description | ID in Application table of the Application that depends on another|
|  | Standards | None|
|  | Validation | Must be an ID of an Application|
|  | Null | Not null|
|  | Automation | None|
| DEPENDENCY | Type | TEXT|
|  | Description | ID in Application table of the Application being depended upon|
|  | Standards | None|
|  | Validation | Must be an ID of an Application|
|  | Null | Not null|
|  | Automation | None|

# Documentation

## Description

The Documentation table records documents that describe Applications or Studies.

## Standards

dc:title; dc:created

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_DOCUMENTATION |  | |
|  | Type | TEXT|
|  | Description | Unique identifier for the Documentation|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| TITLE | Type | TEXT|
|  | Description | Title of the documentation|
|  | Standards | dc:title|
|  | Validation | String|
|  | Automation | None|
| DATE | Type | TEXT|
|  | Description | Date the documentation was created|
|  | Standards | dc:created; ISO8601|
|  | Validation | Datetime string|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| DOCUMENTS | Type | TEXT|
|  | Description | ID in Application table of the Application this Documentation describes|
|  | Standards | dc:relation|
|  | Validation | Must be an ID of an Application|
|  | Null | Null if REFERENCES is not null|
|  | Automation | None|
| DESCRIBES | Type | TEXT|
|  | Description | ID in Study table of the Study this Documentation references|
|  | Standards | dc:relation|
|  | Validation | Must be an ID of a Study|
|  | Null | Null if DOCUMENTS is not null|
|  | Automation | None|

# Employs

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The Employs table records that a StatisticalMethod or VisualisationMethod employs a StatisticalVariable.

## Standards

None

## Automation

This relationship may be inferred automatically from the definitions of methods and variables.

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| STATISTICAL_METHOD |  | |
|  | Type | TEXT|
|  | Description | ID in StatisticalMethod table if the relationship involves a statistical method|
|  | Standards | None|
|  | Validation | Must be an ID of a StatisticalMethod|
|  | Null | Null if VISUALISATION_METHOD is not null|
|  | Automation | None|
| VISUALISATION_METHOD |  | |
|  | Type | TEXT|
|  | Description | ID in VisualisationMethod table if the relationship involves a visualisation method|
|  | Standards | None|
|  | Validation | Must be an ID of a VisualisationMethod|
|  | Null | Null if STATISTICAL_METHOD is not null|
|  | Automation | None|
| STATISTICAL_VARIABLE |  | |
|  | Type | TEXT|
|  | Description | ID in StatisticalVariable table of the variable being employed|
|  | Standards | None|
|  | Validation | Must be an ID of a StatisticalVariable|
|  | Null | Not null|
|  | Automation | None|

# Entailment

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The Entailment table records that a StatisticalMethod or VisualisationMethod entails an Assumption.

## Standards

None

## Automation

This relationship may be inferred automatically from the definitions of methods and assumptions.

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| STATISTICAL_METHOD |  | |
|  | Type | TEXT|
|  | Description | ID in StatisticalMethod table if the relationship involves a statistical method|
|  | Standards | None|
|  | Validation | Must be an ID of a StatisticalMethod|
|  | Null | Null if VISUALISATION_METHOD is not null|
|  | Automation | None|
| VISUALISATION_METHOD |  | |
|  | Type | TEXT|
|  | Description | ID in VisualisationMethod table if the relationship involves a visualisation method|
|  | Standards | None|
|  | Validation | Must be an ID of a VisualisationMethod|
|  | Null | Null if STATISTICAL_METHOD is not null|
|  | Automation | None|
| ASSUMPTION | Type | TEXT|
|  | Description | ID in Assumption table of the Assumption that is entailed|
|  | Standards | None|
|  | Validation | Must be an ID of an Assumption|
|  | Null | Not null|
|  | Automation | None|

# Implements

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The Implements table records that an Application implements a StatisticalMethod or VisualisationMethod.

## Standards

None

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| FUNCTION | Type | TEXT|
|  | Description | Name of the function within the Application that implements the method|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|
| LIBRARY | Type | TEXT|
|  | Description | Name of the library within which the function is found|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| STATISTICAL_METHOD |  | |
|  | Type | TEXT|
|  | Description | ID in StatisticalMethod table if the implementation is for a statistical method|
|  | Standards | None|
|  | Validation | Must be an ID of a StatisticalMethod|
|  | Null | Null if VISUALISATION_METHOD is not null|
|  | Automation | None|
| VISUALISATION_METHOD |  | |
|  | Type | TEXT|
|  | Description | ID in VisualisationMethod table if the implementation is for a visualisation method|
|  | Standards | None|
|  | Validation | Must be an ID of a VisualisationMethod|
|  | Null | Null if STATISTICAL_METHOD is not null|
|  | Automation | None|
| APPLICATION | Type | TEXT|
|  | Description | ID in Application table of the Application implementing the method|
|  | Standards | None|
|  | Validation | Must be an ID of an Application|
|  | Null | Not null|
|  | Automation | None|

# Input

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The Input table records the Boxes that are used as input to a Process, including how they are used.

## Standards

PROV:used

## Automation

Populated automatically when a Process is invoked and its inputs are identified.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| USAGE | Type | TEXT|
|  | Description | Indicates how the input is used by the Process|
|  | Standards | None|
|  | Validation | One of 'dependency' or 'data'|
|  | Automation | Set automatically based on the role of the input|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| PROCESS | Type | TEXT|
|  | Description | ID in Process table of the Process using the input|
|  | Standards | PROV:used|
|  | Validation | Must be an ID of a Process|
|  | Null | Not null|
|  | Automation | Populated automatically when the Process is created|
| BOX | Type | TEXT|
|  | Description | ID in Box table of the Box being used as input|
|  | Standards | PROV:Entity|
|  | Validation | Must be an ID of a Box|
|  | Null | Not null|
|  | Automation | Populated automatically when inputs are resolved|

# Involvement

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The Involvement table records the involvement of a Person in a Study, including their role.

## Standards

PROV:wasAssociatedWith

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ROLE | Type | TEXT|
|  | Description | Role of the Person in the Study|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| PERSON | Type | TEXT|
|  | Description | ID in Person table of the Person involved|
|  | Standards | PROV:Agent|
|  | Validation | Must be an ID of a Person|
|  | Null | Not null|
|  | Automation | None|
| STUDY | Type | TEXT|
|  | Description | ID in Study table of the Study the Person is involved in|
|  | Standards | PROV:Activity|
|  | Validation | Must be an ID of a Study|
|  | Null | Not null|
|  | Automation | None|

# Meets

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The Meets table records that a Computer meets a specified Specification.

## Standards

None

## Automation

None

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| COMPUTER_SPECIFICATION |  | |
|  | Type | TEXT|
|  | Description | ID in Specification table describing the specification met by the Computer|
|  | Standards | None|
|  | Validation | Must be an ID of a Specification|
|  | Null | Not null|
|  | Automation | None|
| REQUIREMENT_SPECIFICATION |  | |
|  | Type | TEXT|
|  | Description | ID in Specification table defining the required specification being met|
|  | Standards | None|
|  | Validation | Must be an ID of a Specification|
|  | Null | Not null|
|  | Automation | None|

# Model

## Description

The Model table identifies Applications that represent models, optionally linking to external model registries.

## Standards

None

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_MODEL | Type | TEXT|
|  | Description | Unique identifier for the Model|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| COMSES | Type | TEXT|
|  | Description | Reference to an entry in the CoMSES-Net model repository|
|  | Standards | None|
|  | Validation | String or identifier|
|  | Null | Optional|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| APPLICATION | Type | TEXT|
|  | Description | ID in Application table of the Application that is a Model|
|  | Standards | None|
|  | Validation | Must be an ID of an Application|
|  | Null | Not null|
|  | Automation | None|

# Parameter

## Description

The Parameter table records parameters used by StatisticalMethod or VisualisationMethod.

## Standards

None

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_PARAMETER | Type | TEXT|
|  | Description | Unique identifier for the Parameter|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| DATA_TYPE | Type | TEXT|
|  | Description | Data type of the parameter|
|  | Standards | XSD|
|  | Validation | Valid XSD data type or URI|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| STATISTICAL_METHOD |  | |
|  | Type | TEXT|
|  | Description | ID in StatisticalMethod table if the parameter applies to a statistical method|
|  | Standards | None|
|  | Validation | Must be an ID of a StatisticalMethod|
|  | Null | Null if VISUALISATION_METHOD is not null|
|  | Automation | None|
| VISUALISATION_METHOD |  | |
|  | Type | TEXT|
|  | Description | ID in VisualisationMethod table if the parameter applies to a visualisation method|
|  | Standards | None|
|  | Validation | Must be an ID of a VisualisationMethod|
|  | Null | Null if STATISTICAL_METHOD is not null|
|  | Automation | None|

# Person

## Description

The Person table records individuals associated with the system, such as users, contributors, or data owners.

## Standards

PROV:Agent; FOAF

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_PERSON | Type | TEXT|
|  | Description | Unique identifier for the Person|
|  | Standards | FOAF|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| EMAIL | Type | TEXT|
|  | Description | Email address of the Person|
|  | Standards | FOAF|
|  | Validation | Valid email address string|
|  | Automation | None|

# PersonalData

## Description

The PersonalData table records additional pieces of information about a Person as label–value pairs.

## Standards

None

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_PERSONAL_DATA |  | |
|  | Type | TEXT|
|  | Description | Unique identifier for the PersonalData entry|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| CATEGORY | Type | TEXT|
|  | Description | Category describing the type of personal data|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|
| VALUE | Type | TEXT|
|  | Description | Value of the personal data|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ABOUT | Type | TEXT|
|  | Description | ID in Person table of the Person this data is about|
|  | Standards | None|
|  | Validation | Must be an ID of a Person|
|  | Null | Not null|
|  | Automation | None|

# Pipeline

## Description

The Pipeline table records sequences of Applications, allowing workflows to be defined where one Application calls another.

## Standards

None

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_PIPELINE | Type | TEXT|
|  | Description | Unique identifier for the Pipeline|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| CALLS | Type | TEXT|
|  | Description | ID in Application table of the Application called by this Pipeline step|
|  | Standards | None|
|  | Validation | Must be an ID of an Application|
|  | Null | Not null|
|  | Automation | None|
| PREVIOUS | Type | TEXT|
|  | Nullable | True|
|  | Description | ID in Pipeline table of the previous Pipeline step|
|  | Standards | None|
|  | Validation | Must be an ID of a Pipeline|
|  | Null | Null if this is the first step|
|  | Automation | None|

# Process

## Description

The Process table records an execution of an Application, including when and how it was run.

## Standards

PROV:Activity

## Automation

Entries are created automatically when an Application is executed, capturing runtime details.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_PROCESS | Type | TEXT|
|  | Description | Unique identifier for the Process|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| START_TIME | Type | TEXT|
|  | Description | Time at which the Process started|
|  | Standards | ISO8601|
|  | Validation | Datetime string|
|  | Automation | Captured automatically at process start|
| END_TIME | Type | TEXT|
|  | Description | Time at which the Process ended|
|  | Standards | ISO8601|
|  | Validation | Datetime string|
|  | Automation | Captured automatically at process completion|
| ARGV | Type | TEXT|
|  | Description | Command-line string used to invoke the Application|
|  | Standards | POSIX|
|  | Validation | String|
|  | Automation | Constructed automatically from Argument and ArgumentValue|
| ENVIRONMENT | Type | TEXT|
|  | Description | Environment variables used during execution|
|  | Standards | POSIX|
|  | Validation | List of strings|
|  | Automation | Captured from runtime environment|
| WORKING_DIR | Type | TEXT|
|  | Description | Working directory from which the Process was executed|
|  | Standards | POSIX|
|  | Validation | Valid file path|
|  | Automation | Captured automatically from runtime|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| EXECUTABLE | Type | TEXT|
|  | Description | ID in Application table of the Application that was executed|
|  | Standards | PROV:used|
|  | Validation | Must be an ID of an Application|
|  | Null | Not null|
|  | Automation | Set when the Process is created|
| SOME_USER | Type | TEXT|
|  | Description | ID in User table of the user who initiated the Process|
|  | Standards | PROV:wasAssociatedWith|
|  | Validation | Must be an ID of a User|
|  | Null | Not null|
|  | Automation | Captured from system user context|
| HOST | Type | TEXT|
|  | Description | ID in Computer table of the machine on which the Process ran|
|  | Standards | PROV:wasAssociatedWith|
|  | Validation | Must be an ID of a Computer|
|  | Null | Not null|
|  | Automation | Captured from system environment|
| PARENT | Type | TEXT|
|  | Description | ID in Process table of the parent Process, if any|
|  | Standards | PROV:wasInformedBy|
|  | Validation | Must be an ID of a Process|
|  | Null | Null if no parent process|
|  | Automation | Set if Process is spawned by another|

# Product

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The Product table describes the types of output that an Application can produce, including how those outputs are located.

## Standards

None

## Automation

Some Products may be inferred automatically based on Application execution and generated Boxes.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| OPTIONALITY | Type | TEXT|
|  | Description | Whether the Product is always produced or only under certain conditions|
|  | Standards | None|
|  | Validation | One of 'always' or 'depends'|
|  | Automation | None|
| LOCATOR | Type | TEXT|
|  | Description | Description of how to locate the Product output|
|  | Standards | None|
|  | Validation | Formatted rule string|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| APPLICATION | Type | TEXT|
|  | Description | ID in Application table of the Application producing this Product|
|  | Standards | None|
|  | Validation | Must be an ID of an Application|
|  | Null | Not null|
|  | Automation | None|
| BOX_TYPE | Type | TEXT|
|  | Description | ID in BoxType table describing the type of Box produced|
|  | Standards | None|
|  | Validation | Must be an ID of a BoxType|
|  | Null | Not null|
|  | Automation | None|
| IN_FILE | Type | TEXT|
|  | Description | ID in BoxType table if the Product is contained within another file|
|  | Standards | None|
|  | Validation | Must be an ID of a BoxType|
|  | Null | Null if LOCATOR is not 'in-file'|
|  | Automation | None|

# Project

## Description

The Project table records Projects, which are collections of Studies and may include funding and organisational information.

## Standards

None

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_PROJECT | Type | TEXT|
|  | Description | Unique identifier for the Project|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| TITLE | Type | TEXT|
|  | Description | Title of the Project|
|  | Standards | dc:title|
|  | Validation | String|
|  | Automation | None|
| FUNDER | Type | TEXT|
|  | Description | Organisation or body funding the Project|
|  | Standards | dc:publisher|
|  | Validation | String|
|  | Automation | None|
| GRANT_ID | Type | TEXT|
|  | Description | Identifier of the grant funding the Project|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| STUDY | Type | TEXT|
|  | Description | A Study is a piece of work at some level of aggregation.|
|  | Standards | None|
|  | Validation | An ID in the Study table.|
|  | Null | Not Null|
|  | Automation | None|

# Requirement

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The Requirement table records requirements that an Application has with respect to Specifications, including exact, minimum, or matching constraints.

## Standards

None

## Automation

None

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| APPLICATION | Type | TEXT|
|  | Description | ID in Application table of the Application that has the requirement|
|  | Standards | None|
|  | Validation | Must be an ID of an Application|
|  | Null | Not null|
|  | Automation | None|
| MATCH | Type | TEXT|
|  | Description | ID in Specification table specifying values that must match|
|  | Standards | None|
|  | Validation | Must be an ID of a Specification|
|  | Null | Null if EXACT or MINIMUM is used|
|  | Automation | None|
| MINIMUM | Type | TEXT|
|  | Description | ID in Specification table specifying minimum acceptable values|
|  | Standards | None|
|  | Validation | Must be an ID of a Specification|
|  | Null | Null if EXACT or MATCH is used|
|  | Automation | None|
| EXACT | Type | TEXT|
|  | Description | ID in Specification table specifying exact required values|
|  | Standards | None|
|  | Validation | Must be an ID of a Specification|
|  | Null | Null if MATCH or MINIMUM is used|
|  | Automation | None|

# Specification

## Description

The Specification table defines labelled specification values, typically used to describe properties of Computers or requirements of Applications.

## Standards

None

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_SPECIFICATION |  | |
|  | Type | TEXT|
|  | Description | Unique identifier for the Specification|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| CATEGORY | Type | TEXT|
|  | Description | Category describing the type of specification|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|
| VALUE | Type | TEXT|
|  | Description | Value of the specification|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| SPECIFICATION_OF |  | |
|  | Type | TEXT|
|  | Description | ID in Computer table of the Computer this Specification describes|
|  | Standards | None|
|  | Validation | Must be an ID of a Computer|
|  | Null | Optional|
|  | Automation | None|

# StatisticalInput

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The StatisticalInput table records the input Variables or Boxes used by a StatisticalMethod when performing a statistical computation.

## Standards

PROV:used

## Automation

Inputs may be inferred automatically when a Statistics computation is executed.

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| STATISTICS | Type | TEXT|
|  | Description | ID in StatisticalMethod table of the method using the input|
|  | Standards | PROV:used|
|  | Validation | Must be an ID of a StatisticalMethod|
|  | Null | Not null|
|  | Automation | None|
| VISUALISATION | Type | TEXT|
|  | Description | ID in Visualisations table of the Visualisation used as input to the method|
|  | Standards | PROV:Entity|
|  | Validation | Must be an ID of a Visualisation|
|  | Null | Null if VARIABLE is not null|
|  | Automation | Resolved automatically where possible|
| VALUE | Type | TEXT|
|  | Description | ID in Value table of the Variable used as input to the method|
|  | Standards | None|
|  | Validation | Must be an ID of a Value|
|  | Null | Null if Value is not null|
|  | Automation | Resolved automatically from Content definitions|

# StatisticalMethod

## Description

The StatisticalMethod table records statistical methods that may be applied to data to generate StatisticalVariables.

## Standards

None

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_STATISTICAL_METHOD |  | |
|  | Type | TEXT|
|  | Description | Unique identifier for the StatisticalMethod|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|

# StatisticalVariable

## Description

The StatisticalVariable table records variables that are generated by applying a StatisticalMethod.

## Standards

None

## Automation

StatisticalVariables may be created automatically as outputs of statistical computations.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_STATISTICAL_VARIABLE |  | |
|  | Type | TEXT|
|  | Description | Unique identifier for the StatisticalVariable|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| DATA_TYPE | Type | TEXT|
|  | Description | Data type of the StatisticalVariable|
|  | Standards | XSD|
|  | Validation | Valid XSD data type or URI|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| STATISTIC_GENERATED_BY |  | |
|  | Type | TEXT|
|  | Description | ID in StatisticalMethod table of the method that generates this StatisticalVariable|
|  | Standards | PROV:wasGeneratedBy|
|  | Validation | Must be an ID of a StatisticalMethod|
|  | Null | Not null|
|  | Automation | None|
| VISUALISATION_GENERATED_BY |  | |
|  | Type | TEXT|
|  | Description | ID in VisualisationMethod table of the method that generates this Visualisation|
|  | Standards | PROV:wasGeneratedBy|
|  | Validation | Must be an ID of a VisualisationMethod.|
|  | Null | Not null|
|  | Automation | None|

# Statistics

## Description

The Statistics table records statistical computations, including when they were performed and how input data was selected.

## Standards

PROV:Activity

## Automation

Entries may be created automatically when statistical computations are performed.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_STATISTICS | Type | TEXT|
|  | Description | Unique identifier for the Statistics computation|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| DATE | Type | DATE|
|  | Description | Date the statistical computation was performed|
|  | Standards | ISO8601|
|  | Validation | Datetime string|
|  | Automation | Set automatically at execution time|
| QUERY | Type | TEXT|
|  | Description | Query used to select the data for the statistical computation|
|  | Standards | None|
|  | Validation | Formatted string|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| USED | Type | TEXT|
|  | Description | ID in StatisticalMethod table of the method used for the computation|
|  | Standards | PROV:used|
|  | Validation | Must be an ID of a StatisticalMethod|
|  | Null | Not null|
|  | Automation | Set when the Statistics entry is created|

# Study

## Description

The Study table records units of scientific work, representing collections of Processes, data, and outputs.

## Standards

PROV:Activity

## Automation

Some fields may be populated automatically when Processes are grouped into Studies.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_STUDY | Type | TEXT|
|  | Description | Unique identifier for the Study|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| TITLE | Type | TEXT|
|  | Description | Title or name of the Study|
|  | Standards | dc:title|
|  | Validation | String|
|  | Automation | None|
| START_TIME | Type | DATE|
|  | Description | Start time of the Study|
|  | Standards | ISO8601|
|  | Validation | Datetime string|
|  | Automation | May be inferred from earliest Process|
| END_TIME | Type | DATE|
|  | Description | End time of the Study|
|  | Standards | ISO8601|
|  | Validation | Datetime string|
|  | Automation | May be inferred from latest Process|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| PROJECT | Type | TEXT|
|  | Description | ID in Project table of the Project this Study belongs to|
|  | Standards | None|
|  | Validation | Must be an ID of a Project|
|  | Null | Optional|
|  | Automation | None|
| PART | Type | TEXT|
|  | Description | ID in Study table if this Study is part of another Study|
|  | Standards | PROV:wasPartOf|
|  | Validation | Must be an ID of a Study|
|  | Null | Null if not part of another Study|
|  | Automation | None|

# Tag

## Description

The Tag table records tags that can be used to classify and annotate other entities in the system.

## Standards

None

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_TAG | Type | TEXT|
|  | Description | Unique identifier for the Tag|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|

# TagMap

This is reification. In the graph database, this will appear as an edge between two entites. In a relational database, this will be a relation which allows the enumeration of the many-to-many linkage.

## Description

The TagMap table records the association of Tags with other entities such as Applications, Boxes, Documentation, Studies, and Methods.

## Standards

None

## Automation

Tags may be applied manually by users or inferred automatically based on metadata and usage.

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| TAG | Type | TEXT|
|  | Description | ID in Tag table of the Tag being applied|
|  | Standards | None|
|  | Validation | Must be an ID of a Tag|
|  | Null | Not null|
|  | Automation | None|
| APPLICATION | Type | TEXT|
|  | Description | ID in Application table if the Tag applies to an Application|
|  | Standards | None|
|  | Validation | Must be an ID of an Application|
|  | Null | Null if not applicable|
|  | Automation | None|
| ASSUMPTION | Type | TEXT|
|  | Description | ID in Assumptoin table if the Tag applies to an Assumption.|
|  | Standards | None|
|  | Validation | Must be an ID of an Assumption|
|  | Null | Null if not applicable|
|  | Automation | None|
| BOX | Type | TEXT|
|  | Description | ID in Box table if the Tag applies to a Box|
|  | Standards | None|
|  | Validation | Must be an ID of a Box|
|  | Null | Null if not applicable|
|  | Automation | None|
| BOX_TYPE | Type | TEXT|
|  | Description | ID in BoxType table if the Tag applies to a BoxType|
|  | Standards | None|
|  | Validation | Must be an ID of a BoxType|
|  | Null | Null if not applicable|
|  | Automation | None|
| DOCUMENTATION | Type | TEXT|
|  | Description | ID in Documentation table if the Tag applies to Documentation|
|  | Standards | None|
|  | Validation | Must be an ID of a Documentation|
|  | Null | Null if not applicable|
|  | Automation | None|
| OTHER_TAG | Type | TEXT|
|  | Description | ID in Tag table if the Tag relates to another Tag|
|  | Standards | None|
|  | Validation | Must be an ID of a Tag|
|  | Null | Null if not applicable|
|  | Automation | None|
| PERSON | Type | TEXT|
|  | Description | ID in Person table is the Person in the Person table.|
|  | Standards | None|
|  | Validation | Must be an ID of a Tag|
|  | Null | Null if not applicable|
|  | Automation | None|
| STATISTICAL_METHOD |  | |
|  | Type | TEXT|
|  | Description | ID in StatisticalMethod table if the Tag applies to a statistical method|
|  | Standards | None|
|  | Validation | Must be an ID of a StatisticalMethod|
|  | Null | Null if not applicable|
|  | Automation | None|
| STUDY | Type | TEXT|
|  | Description | ID in Study table if the Tag applies to a Study|
|  | Standards | None|
|  | Validation | Must be an ID of a Study|
|  | Null | Null if not applicable|
|  | Automation | None|
| VISUALISATION_METHOD |  | |
|  | Type | TEXT|
|  | Description | ID in VisualisationMethod table if the Tag applies to a visualisation method|
|  | Standards | None|
|  | Validation | Must be an ID of a VisualisationMethod|
|  | Null | Null if not applicable|
|  | Automation | None|

# User

## Description

The User table records system user accounts, linking operating system user information to a Person.

## Standards

PROV:Agent

## Automation

Most values are obtained automatically from the operating system.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_USER | Type | TEXT|
|  | Description | Unique identifier for the User|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| HOME_DIR | Type | TEXT|
|  | Description | Home directory of the user|
|  | Standards | POSIX|
|  | Validation | Valid file path|
|  | Automation | Retrieved from the operating system|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ACCOUNT_OF | Type | TEXT|
|  | Description | ID in Person table of the Person this User account belongs to|
|  | Standards | PROV:actedOnBehalfOf|
|  | Validation | Must be an ID of a Person|
|  | Null | Not null|
|  | Automation | Resolved from system/user configuration|

# Uses

## Description

The Uses table records that an Application uses a BoxType as an input or dependency.

## Standards

PROV:used

## Automation

May be inferred automatically based on Application execution and detected Inputs.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| LOCATOR | Type | TEXT|
|  | Description | Description of how to locate the Uses input|
|  | Standards | None|
|  | Validation | Formatted rule string|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| APPLICATION | Type | TEXT|
|  | Description | ID in Application table of the Application that uses the input|
|  | Standards | PROV:Activity|
|  | Validation | Must be an ID of an Application|
|  | Null | Not null|
|  | Automation | None|
| BOX_TYPE | Type | TEXT|
|  | Description | ID in BoxType table of the type of Box that is used|
|  | Standards | PROV:Entity|
|  | Validation | Must be an ID of a BoxType|
|  | Null | Not null|
|  | Automation | None|
| IN_FILE | Type | TEXT|
|  | Description | ID in BoxType table if the Uses input is contained within another file|
|  | Standards | None|
|  | Validation | Must be an ID of a BoxType|
|  | Null | Null if LOCATOR is not 'in-file'|
|  | Automation | None|

# Value

## Description

The Value table represents values of Variables or StatisticalVariables. It is a virtual table whose entries are retrieved from Boxes rather than stored directly.

## Standards

PROV:Entity

## Automation

Values are not stored explicitly; they are retrieved dynamically from Boxes based on Content specifications.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_VALUE | Type | TEXT|
|  | Constraint | PRIMARY KEY|
|  | Description | Identifier or representation of the value|
|  | Standards | None|
|  | Validation | This should be a unique string|
|  | Automation | Retrieved from underlying data in Box|
| UNITS | Type | TEXT|
|  | Description | The units of the value.|
|  | Standards | None|
|  | Validation | None|
|  | Automation | None.|
| FORMAT | Type | TEXT|
|  | Description | ID in Variable table of the Variable this Value corresponds to|
|  | Standards | None|
|  | Validation | Values are not alway numbers.|
|  | Automation | None.|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| VARIABLE | Type | TEXT|
|  | Description | ID in Variable table of the Variable this Value corresponds to|
|  | Standards | None|
|  | Validation | Must be an ID of a Variable|
|  | Null | Null if STATISTICAL_VARIABLE is used|
|  | Automation | Resolved via Content definitions|
| STATISTICAL_VARIABLE |  | |
|  | Type | TEXT|
|  | Description | ID in StatisticalVariable table if this Value is the result of a statistical computation|
|  | Standards | None|
|  | Validation | Must be an ID of a StatisticalVariable|
|  | Null | Null if VARIABLE is used|
|  | Automation | Resolved via statistical processing|
| PARAMETER | Type | TEXT|
|  | Description | ID in Parameter table if this Value corresponds to a parameter|
|  | Standards | None|
|  | Validation | Must be an ID of a Parameter|
|  | Null | Optional|
|  | Automation | Resolved during method execution|
| STATISTICAL_PARAMETER |  | |
|  | Type | TEXT|
|  | Description | ID in Statistics table if this Value corresponds to a Statistic|
|  | Standards | None|
|  | Validation | Must be an ID of a Statistic|
|  | Null | Optional|
|  | Automation | Resolved during method execution|
| VISUALISATION_PARAMETER |  | |
|  | Type | TEXT|
|  | Description | ID in the Visualisation table if this Value corresponds to a Visualisation|
|  | Standards | None|
|  | Validation | Must be an ID of a Visualisation|
|  | Null | Optional|
|  | Automation | Resolved during method execution|
| RESULT_OF | Type | TEXT|
|  | Description | ID in Statistics table if this Value is the result of a statistical computation|
|  | Standards | PROV:wasGeneratedBy|
|  | Validation | Must be an ID of a Statistics|
|  | Null | Optional|
|  | Automation | Set when statistical outputs are generated|
| TIME | Type | TEXT|
|  | Description | ID in Context table representing the time associated with the Value|
|  | Standards | None|
|  | Validation | Must be an ID of a Context|
|  | Null | Optional|
|  | Automation | Derived from Content locators|
| SPACE | Type | TEXT|
|  | Description | ID in Context table representing the spatial context of the Value|
|  | Standards | None|
|  | Validation | Must be an ID of a Context|
|  | Null | Optional|
|  | Automation | Derived from Content locators|
| AGENT | Type | TEXT|
|  | Description | ID in Context table representing the agent associated with the Value|
|  | Standards | None|
|  | Validation | Must be an ID of a Context|
|  | Null | Optional|
|  | Automation | Derived from Content locators|
| LINK | Type | TEXT|
|  | Description | ID in Context table representing link relationships associated with the Value|
|  | Standards | None|
|  | Validation | Must be an ID of a Context|
|  | Null | Optional|
|  | Automation | Derived from Content locators|
| CONTAINED_IN | Type | TEXT|
|  | Description | ID in Box table from which the Value is retrieved|
|  | Standards | PROV:Entity|
|  | Validation | Must be an ID of a Box|
|  | Null | Not null|
|  | Automation | Determined from data source|

# Variable

## Description

The Variable table records variables that describe data, including their name, type, and roles such as time, space, agent, or link.

## Standards

None

## Automation

Variables are generally defined by the user; some roles may be inferred during data processing.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_VARIABLE | Type | TEXT|
|  | Description | Identifier of the variable|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | None|
| NAME | Type | TEXT|
|  | Description | Name of the variable|
|  | Standards | None|
|  | Validation | String|
|  | Automation | None|
| DATA_TYPE | Type | TEXT|
|  | Description | Data type of the variable|
|  | Standards | XSD|
|  | Validation | Valid XSD data type or URI|
|  | Automation | None|
| IS_AGENT | Type | INTEGER|
|  | Description | Indicates whether this variable represents an agent identifier|
|  | Standards | None|
|  | Validation | True or False|
|  | Automation | None|
| IS_LINK | Type | INTEGER|
|  | Description | Indicates whether this variable represents a link identifier|
|  | Standards | None|
|  | Validation | True or False|
|  | Automation | None|
| IS_SPACE | Type | INTEGER|
|  | Description | Indicates whether this variable represents spatial information|
|  | Standards | None|
|  | Validation | True or False|
|  | Automation | None|
| IS_TIME | Type | INTEGER|
|  | Description | Indicates whether this variable represents temporal information|
|  | Standards | None|
|  | Validation | True or False|
|  | Automation | None|

# Visualisation

## Description

The Visualisation table records visualisations generated from data, including when they were created and how the data was selected.

## Standards

PROV:Activity

## Automation

Entries may be created automatically when a visualisation is generated.


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_VISUALISATION |  | |
|  | Type | TEXT|
|  | Description | Unique identifier for the Visualisation|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|
| DATE | Type | DATE|
|  | Description | Date the Visualisation was created|
|  | Standards | ISO8601|
|  | Validation | Datetime string|
|  | Automation | Set automatically at creation time|
| QUERY | Type | TEXT|
|  | Description | Query used to select data for the Visualisation|
|  | Standards | None|
|  | Validation | Formatted string|
|  | Automation | None|

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| VISUALISATION_METHOD |  | |
|  | Type | TEXT|
|  | Description | ID in VisualisationMethod table of the method used to generate the Visualisation|
|  | Standards | PROV:used|
|  | Validation | Must be an ID of a VisualisationMethod|
|  | Null | Not null|
|  | Automation | Set when the Visualisation is created|
| CONTAINED_IN | Type | TEXT|
|  | Description | ID in Box table of the Box containing the Visualisation|
|  | Standards | PROV:Entity|
|  | Validation | Must be an ID of a Box|
|  | Null | Optional|
|  | Automation | Set if output is stored in a Box|

# VisualisationMethod

## Description

The VisualisationMethod table records methods used to generate visualisations from data.

## Standards

None

## Automation

None


##  Attributes

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| ID_VISUALISATION_METHOD |  | |
|  | Type | TEXT|
|  | Description | Unique identifier for the VisualisationMethod|
|  | Standards | None|
|  | Validation | Must be unique|
|  | Automation | Automated by the instantiating framework|

# VisualisationValue

## Description

The VisualisationValue table links Values to Visualisations, indicating which Values are used in a given Visualisation.

## Standards

PROV:used

## Automation

Entries are created automatically when a Visualisation is generated.

##  Relationships

| Field    |Property| Value                   |
|----------|--------|-------------------------|
| VALUE | Type | TEXT|
|  | Description | ID in Value table of the Value used in the Visualisation|
|  | Standards | PROV:Entity|
|  | Validation | Must be an ID of a Value|
|  | Null | Not null|
|  | Automation | Populated automatically when the Visualisation is created|
| VISUALISATION | Type | TEXT|
|  | Description | ID in Visualisation table of the Visualisation using the Value|
|  | Standards | PROV:Activity|
|  | Validation | Must be an ID of a Visualisation|
|  | Null | Not null|
|  | Automation | Populated automatically when the Visualisation is created|


