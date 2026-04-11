# Changelog

## [v2.1.3] - 2024-04-04

> **From this version, the Docker image is published on Docker Hub. Change the `image` field in `docker-compose.yml` from `ghcr.io/subconv/subconv:latest` to `wouisb/subconv:latest`.**

### Fixes

- Make [Vercel](https://vercel.com) happy

**Full Changelog**: https://github.com/SubConv/SubConv/compare/v2.1.2...v2.1.3

## [v2.1.2] - 2024-03-24

### Fixes

- [core] Add back support for Clash Meta <= v1.15.1 (#30)
- [ui] Fix title of the web page (#31)
- [config] Fix config generation & error handling (#32)

**Full Changelog**: https://github.com/SubConv/SubConv/compare/v2.1.0...v2.1.2

## [v2.1.1] - 2024-02-15

**Full Changelog**: https://github.com/SubConv/SubConv/compare/v2.1.0...v2.1.1

## [v2.1.0] - 2024-02-14

### Breaking Changes

- Change default port (#22)

### Fixes

- Handle redirect (#21)
- Fix fatal error in redirect handling (#23)

### Improvements

- Change default port (#22)

**Full Changelog**: https://github.com/SubConv/SubConv/compare/v2.0.0...v2.1.0

## [v2.0.0] - 2024-02-10

### Features

- Support Docker; CI build and build image; CI release (#17)
- CLI to generate config file (#18)

### Breaking Changes

Please refer to [docs](https://subconv.is-sb.com) for configuration.

- Support config for headers (like DNS, etc.) (#14)
- Use YAML config (#16)

**Full Changelog**: https://github.com/SubConv/SubConv/compare/v1.0.0...v2.0.0

## [v1.0.0] - 2024-02-08

### Breaking Changes

- Remove `region_dict` in config file because it duplicates the function of `regex` field.

### Changes

- Use rule-provider

### Features

- Support proxy of url of rulesets to ensure that rulesets can be downloaded.
