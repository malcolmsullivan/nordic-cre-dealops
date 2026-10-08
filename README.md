# Nordic CRE DealOps Desk

A backend API that helps commercial real estate brokers and investors
track property ownership and portfolios so they can identify opportunities.

## The problem

Finding the parent company behind a property-owning legal entity, and the
principals behind that parent, is slow work. In brokerage practice the
information is scattered across multiple tabs and tools, and the link
between a property, its owning entity and the people behind it is rarely
recorded in one place.

## What it will do

- Store properties, legal entities, contacts and deals in a relational
  PostgreSQL database.
- Model ownership chains (property, owning entity, parent company,
  principals) and answer questions such as "which other properties does
  this principal control through any entity?"
- Track interactions with contacts and the stage of each deal.
- Expose all of this through a documented REST API.

## Data

Company and market statistics will come from free public Swedish sources
where available. Ownership links, contacts, interactions and deals are
synthetic, because no free source provides them. No real personal or
confidential data is used.

## Tech

Python, PostgreSQL, FastAPI (planned), pytest (planned).

## Status

Early setup. Nothing is deployed yet.