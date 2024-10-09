<h1>Helsinki Electricity Usage</h1>

This is a data pipeline to pull public Helsinki electricity usage from [Nuuka Open API](https://helsinki-openapi.nuuka.cloud/swagger/index.html) and load it into a data warehouse.

<h2>Architecture</h2>

![metabase_connection_settings](https://github.com/antinaho/electricityMonitor/raw/master/assets/pipeline.png?raw=true)

We use python to pull, transform and load data. Our warehouse is postgres. We also spin up a Metabase instance for our presentation layer.

Postgres, Metabase and python app run on separate docker containers.

<h2>Basic analysis</h2>

Usage for the whole day, all locations:\
![usage graph for the whole day](https://github.com/antinaho/electricityMonitor/raw/master/assets/daily_electricity_graph.png?raw=true)

Daily usage ranked:\
![usage graph for the whole day](https://github.com/antinaho/electricityMonitor/raw/master/assets/top_5.png?raw=true)

<h2>Run pipeline</h2>
<h4>Run locally</h4>

To run locally you need:
  1. git
  2. Docker

Clone the repo and run the following commands:
```
git clone https://github.com/antinaho/electricityMonitor.git
cd electricityMonitor
docker compose up -d
```
Go to localhost:3000 to see the Metabase UI.\
If you don't see the UI wait ~30 seconds for Metabase to load up

Metabase connection settings:\
![metabase_connection_settings](https://github.com/antinaho/electricityMonitor/raw/master/assets/metabase_connections.png?raw=true)
