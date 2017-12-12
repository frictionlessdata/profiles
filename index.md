# Bootstrapping data standards with Frictionless Data

## Introduction

When it comes to tabular data, the [Frictionless Data][fd] specifications provide users with strong conventions for declaring both the shape of data (via schemas) and information about the data (as metadata on package and resource descriptors).

Within the Frictionless Data world, we purposefully refer to specification work as *specifications*, and not *standards*. The specifications therein provide clear conventions for working with data, and declare fundamental interfaces on which a modular software system that works with these specifications can be built. It is very meta. However, this specifications and software foundation *do* make the Frictionless Data ecosystem a powerful and compelling technical foundation on which to build data standards. Some reasons for why this is so being:

- data serialised in a format that can be read by software developers use to build tools such as APIs, and also by many consumer programs that are used by consumers of data with little to no technical know how.
- built in progressive enhancement, where metadata, as well as structural and schematic information about the data, can be incorporated over time without modifying the original data source.
- A large and growing collection of tools, in many programming languages, for working with the Frictionless Data specifications
- The specifications and the software are platform agnostic. A major example of this is being web-friendly without being dependent on the web (as with many linked data approaches). Linkable data, not Linked Data.

We'll demonstrate this with some examples below, which are a proof of concept for the idea of using Frictionless Data as a technical foundation for data standards. This is an ongoing work that we intend to iterate on in response to feedback to this initial take.

Of course, we do not in any way think that the technical implementation of a data standard is what "data standards" is about. Data standards are about communities of practice, stakeholder engagement, and increasingly, a vehicle of change at the level of policy and governance. Technical implementation, in this wider context, is but a small, yet crucial, component. Indeed, this is a critical part of the promise we are pointing to here - that by building on a common foundation, communities building data standards can focus a little less on the technical implementation details and a little more on the change they want to see by creating them.

## Examples

### Clinical trials

#### Overview

The [WHO Dataset](http://www.who.int/ictrp/network/trds/en/) is a guidance for publishing clinical trial meta data on various public registers. The dataset has 24 fields that should be present to register a clinical trial. In our [Open Trials][ot] project, we based our data schema on the WHO dataset, extending it as required by data we matched onto the core fields.

#### Data

Here is a representative sample of clinical trial metadata, using the WHO Dataset fields, as CSV. This sample contains around 100 data records. The complete dataset on [Open Trials][ot] currently holds around XXXXX records.

See the [example data here](/assets/clinical-trials/data.csv).

TODO: sample data to use.

#### Schema

You will notice on viewing the WHO Dataset documentation, or the sample data we have prepared, that the various fields of data have certain properties - some are simple strings, some are dates, so are numbers. We can capture this information using a [Table Schema][ts] descriptor. Having such a descriptor allows us to perhaps important checks on the data - checks related to "schematic integrity" which are essential to consumption and reuse of this data.

See the [example Table Schema here](/assets/clinical-trials/tableschema.json).

#### Validation

To check our data source is valid according to requirements of our "Clinical trial profile", we write a short spec using JSON Schema. JSON Schema specs are used by most tools in the Frictionless Data ecosystem to ensure correctness of form and content in data. Our Table Schema above says *how* the data should look, and the JSON Schema provides instructions to the tooling check this is so.

TODO: JSON Schema to use

#### Usage

Now that we have some sample data and our schemas, we have everything we need to generate an API for validating and consuming our data. Let's demonstrate in Python.

```
TODO: Python example.
```

### Grant funding

#### Overview

#### Data

TODO: A sample dataset

#### Fields

TODO: Table Schema of required fields
TODO: Wrap TS in a Data Package, use FKs if relevant. Convention of first resource as "fact" table.

#### Validation schema

TODO: Create JSON Schema that validates the Tabular Data Package under a custom profile name

#### Usage

TODO: iterate over table in Python

### Art collections

#### Overview

Copy and adjust as required from https://github.com/cmoa/collection

#### Data

TODO: A sample dataset

#### Fields

TODO: Table Schema of required fields
TODO: Wrap TS in a Data Package, use FKs if relevant. Convention of first resource as "fact" table.

#### Validation schema

TODO: Create JSON Schema that validates the Tabular Data Package under a custom profile name

#### Usage

TODO: iterate over table in Python

### Trees

#### Overview

The [Open Council Data][opencouncildata] defined the standard [Trees 1.3][trees-spec] for describing the trees in a geographical region (e.g. a council). This standard includes information about the location, type, and other characteristics of individual trees, which is useful for planning future growth, maintenance of canopy cover, managing risk of falling branches, etc.

#### Data

We are using the from [Colac Otway Shire Trees][trees-datasource] as an example.

| lat | lon | genus | species | dbh | dbh_min | dbh_max | year_min | year_max | crown | crown_min | crown_max | height | height_min | height_max | common | location | ref | maintenance | maturity | planted | updated | health | variety | description | family | ule_min | ule_max | address |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -38.344595 | 143.592171 | Melaleuca | Stypheliodes | 1 |  |  |  |  |  |  |  | 5 |  |  | Prickly Paperback | street | 10001 |  | mature | 1975-01-01 |  |  |  |  |  |  |  | 106 Queen ST COLAC VIC 3250 |
| -38.346198 | 143.591812 | Melaleuca | Stypheliodes | 1 |  |  |  |  |  |  |  | 4 |  |  | Prickly Paperback | street | 10004 |  | mature | 1975-01-01 |  |  |  |  |  |  |  | 122 Queen ST COLAC VIC 3250 |
| -38.342097 | 143.588944 | Fraxinus | Excelsior | 1.2 |  |  |  |  |  |  |  | 12 |  |  | Golden Ash | street | 10007 |  | mature | 1980-01-01 |  |  |  |  |  |  |  | 40 Rae ST COLAC VIC 3250 |
| -38.341927 | 143.588715 | Agonis | Flexuosa | 0.4 |  |  |  |  |  |  |  | 5 |  |  | Weeping Willow Myrtle | street | 10018 |  | semi-mature | 1980-01-01 |  |  |  |  |  |  |  | 47 Rae ST COLAC VIC 3250//next to coles coaches |
| -38.342044 | 143.591182 | Eucalyptus | Nichollii | 0.3 |  |  |  |  |  |  |  | 6 |  |  | Willow Peppermint | street | 10021 |  | mature | 1980-01-01 |  |  |  |  |  |  |  | 56 Rae ST COLAC VIC 3250//Between Queen St & CCDA |

This data was modified from the source to conform to the [Trees 1.3][trees-spec] specification. All the data is available [here][trees-data].

#### Metadata

The [Trees Data Package][trees-schema] extends the [Data Package][dp] specification by adding the following fields:

| Name               | Description                                                                                     | Type    |
| ---                | ---                                                                                             | ---     |
| countryCode        | A single or an array of 2-letter ISO country code defining the country(ies) present in the data | string  |
| geospatialCoverage | Geospatial area contained in the dataset                                                        | geojson |

#### Fields

| Name | Title | Type | Constraints |
| --- | --- | --- | --- |
| lat | Latitude in decimal degrees (EPSG:4326) | number | **required**: True |
| lon | Longitude in decimal degrees (EPSG:4326) | number | **required**: True |
| genus | Botanical genus, in title case (e.g. Eucalyptus) | string |  |
| species | Botanical species, in title case (e.g. Regnans) | string |  |
| dbh | Diameter at breast height (130cm above ground), in centimeters. If this information is available only as a range, this contains the middle of the range. | number | **minimum**: 0 |
| dbh_min | Minimum diameter at breast height (130cm above ground) | number | **minimum**: 0 |
| dbh_max | Maximum diameter at breast height (130cm above ground) | number | **minimum**: 0 |
| year_min | Lower bound on year that tree is expected to live to (e.g. A tree surveyed in 2008 with useful life expectancy range of 10-15 years would be 2018). | year |  |
| year_max | Upper bound on year that tree is expected to live to (e.g. A tree surveyed in 2008 with useful life expectancy range of 10-15 years would be 2023). | year |  |
| crown | Width in metres of the tree’s foliage (also known as crown spread). If this information is available only as a range, this contains the middle of the range. | number | **minimum**: 0 |
| crown_min | Minimum width in meters of the tree's foliage | number | **minimum**: 0 |
| crown_max | Maximum width in meters of the tree's foliage | number | **minimum**: 0 |
| height | Height in meters. If this information is available only as a range, this contains the middle of the range. | number | **minimum**: 0 |
| height_min | Minimum height in meters | number | **minimum**: 0 |
| height_max | Maximum height in meters | number | **minimum**: 0 |
| common | Common name for species (non-standardised) | string |  |
| location | Where the tree is located | string | **enum**: ['park', 'street', 'council'] |
| ref | Council-specific identifier, enabling joining to other datasets | number |  |
| maintenance | How often the tree is inspected (in months) | number | **minimum**: 0 |
| maturity |  | string | **enum**: ['young', 'semi-mature', 'mature', 'over-mature'] |
| planted | Date of planting | date |  |
| updated | Date of addition to database or most recent revision | date |  |
| health | Health of tree growth | string | **enum**: ['stump', 'dead', 'poor', 'fair', 'good'] |
| variety | Any part of the scientific name below species level, including subspecies or variety | string |  |
| description | Other information about the tree that is not in its scientific name or species | string |  |
| family | Botanical family | string |  |
| ule_min | Lower bound on useful life expectancy when surveyed | number | **minimum**: 0 |
| ule_max | Upper bound on useful life expectancy when surveyed | number | **minimum**: 0 |
| address | Street address | string |  |

#### Usage

```python
import datapackage

datapackage_url = 'https://raw.githubusercontent.com/frictionlessdata/profiles/master/assets/trees/datapackage.json'
dp = datapackage.Package(datapackage_url)

for row in dp.resources[0].iter(keyed=True):
    print(row)
    # {'lat': Decimal('-38.347497'), 'lon': Decimal('143.595686'), 'genus': 'Melaleuca', 'species': 'Nesophila', 'dbh': Decimal('0.25'), 'dbh_min': None, 'dbh_max': None, 'year_min': None, 'year_max': None, 'crown': None, 'crown_min': None, 'crown_max': None, 'height': Decimal('2'), 'height_min': None, 'height_max': None, 'common': 'Snowy Honey Myrtle', 'location': 'street', 'ref': Decimal('10379'), 'maintenance': None, 'maturity': 'semi-mature', 'planted': datetime.date(1980, 1, 1), 'updated': None, 'health': None, 'variety': None, 'description': None, 'family': None, 'ule_min': None, 'ule_max': None, 'address': '18 Thomas ST COLAC VIC 3250'}
```

### Street furniture

#### Overview

Do a data package version of http://standards.opencouncildata.org/#/street-furniture

#### Data

TODO: A sample dataset

#### Fields

TODO: Table Schema of required fields
TODO: Wrap TS in a Data Package, use FKs if relevant. Convention of first resource as "fact" table.

#### Validation schema

TODO: Create JSON Schema that validates the Tabular Data Package under a custom profile name

#### Usage

TODO: iterate over table in Python

### Fiscal data

The above examples demonstrate a simple approach to creating a data standard with the existing Frictionless Data specifications. We are currently working on a v1 release of [Fiscal Data Package][fdp], which takes a different approach; one that we plan to abstract into a general specification in the future. Here, we describe higher-level concepts for the domain hand at via a collection of `columnType` properties that extends [Table Schema][ts]. This work is very much work in progress. The current state of [Fiscal Data Package v1 can be found here][fdpv1].

## Closing

This has been a high-level exploration of using [Tabular Data Package][tdp] and [Table Schema][ts] as a "specification framework", allowing one to bootstrap a proof of concept data standard. Taking this approach, one gains access to a collection of modular software libraries that provide powerful APIs for working with this data according to the rules and condition of the standard that is declared. Data validation, processing, transport, and consumption do not require custom tool chains once the data standard is declared as a [Tabular Data Package Profile][profile].

The approach described here is a first step in the direction of domain-specific tabular data profiles. A future iteration would likely integrate work we are currently undertaking in [Fiscal Data Package][fdp] which enables the simple declaration of *domain concepts* via `columnType` annotations on Table Schemas. This enables data standard authors to work at a level of abstraction of domain concepts, rather than the "primitive types" we work with here via Table Schema. We plan to revisit this work once the `columnType` work from Fiscal Data Package is stable for general use.

For now, all the schemas above work as described, right now, and open up all the software in the Frictionless Data ecosystem to those following this approach.

[fd]: https://frictionlessdata.io
[tdp]: https://frictionlessdata.io/specs/tabular-data-package/
[dp]: https://frictionlessdata.io/specs/data-package/
[fdp]: https://frictionlessdata.io/specs/fiscal-data-package/
[fdpv1]: https://hackmd.io/BwNgpgrCDGDsBMBaAhtALARkWsPEE5posR8RxgAzffWfDIA=
[ts]: https://frictionlessdata.io/specs/table-schema/
[profile]: https://frictionlessdata.io/specs/profiles/
[who]: http://www.who.int/ictrp/network/trds/en/
[ot]: https://opentrials.net
[who-dataset]: http://www.who.int/ictrp/network/trds/en/ "World Health Organisation Trial Registration Data Set"
[opencouncildata]: https://opencouncildata.org/ "Open Council Data"
[trees-data]: assets/trees/data.csv "Trees CSV"
[trees-dp]: assets/trees/datapackage.json "Trees Data Package"
[trees-schema]: assets/trees/trees-data-package "Trees Data Package JSON Schema"
[trees-spec]: http://standards.opencouncildata.org/#/trees "Open Council Data: Trees 1.3 Specification"
[trees-datasource]: https://data.gov.au/dataset/colac-otway-shire-trees/resource/bcf1d62b-9e72-4eca-b183-418f83dedcea "Colac Otway Shire Trees"
