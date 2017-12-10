# Bootstrapping data standards with Frictionless Data

## Introduction

When it comes to tabular data, the [Frictionless Data][fd] specifications provide users with strong conventions for declaring both the shape of data (via schemas) and information about the data (as metadata on package and resource descriptors).

Within the Frictionless Data world, we purposefully refer to specification work as *specifications*, and not *standards*. The specifications therein provide clear conventions for working with data, and declare fundamental interfaces on which a modular software system that works with these specifications can be built. It is very meta. However, this specifications and software foundation *do* make the Frictionless Data ecosystem a powerful and compelling technical foundation on which to build data standards. Some reasons for why this is so being:

- data serialised in a format that can be read by software developers use to build tools such as APIs, and also by many consumer programs that are used by consumers of data with little to no technical know how.
- built in progressive enhancement, where metadata, as well as structural and schematic information about the data, can be incorporated over time without modifying the original data source.
- A large and growing collection of tools, in many programming languages, for working with the Frictionless Data specifications
- The specifications and the software are platform agnostic. A major example of this is being web-friendly without being dependent on the web (as with many linked data approaches). Linkable data, not Linked Data.

We'll demonstrate this by some example below, which are a proof of concept for the idea of using Frictionless Data as a technical foundation for data standards. This is an ongoing work that we intend to iterate on in response to feedback to this initial take.

Of course, we do not in any way think that the technical implementation of a data standard is what "data standards" is about. Data standards are about communities of practice, stakeholder engagement, and increasingly, a vehicle of change at the level of policy and governance. Technical implementation, in this wider context, is but a small, yet crucial, component. Indeed, this is a critical part of the promise we are pointing to here - that by building on a common foundation, communities building data standards can focus a little less on the technical implementation details and a little more on the change we want to see by creating them.

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

Do a data package version of http://standards.opencouncildata.org/#/trees

#### Data

TODO: A sample dataset

#### Fields

TODO: Table Schema of required fields
TODO: Wrap TS in a Data Package, use FKs if relevant. Convention of first resource as "fact" table.

#### Validation schema

TODO: Create JSON Schema that validates the Tabular Data Package under a custom profile name

#### Usage

TODO: iterate over table in Python

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
[fdp]: https://frictionlessdata.io/specs/fiscal-data-package/
[fdpv1]: https://hackmd.io/BwNgpgrCDGDsBMBaAhtALARkWsPEE5posR8RxgAzffWfDIA=
[ts]: https://frictionlessdata.io/specs/table-schema/
[profile]: https://frictionlessdata.io/specs/profiles/
[who]: http://www.who.int/ictrp/network/trds/en/
[ot]: https://opentrials.net
