# How to play

1. Install the python packages:
   `pip install -r requirements.txt`

2. In the root directory of this repo, run `run.sh`.

3. Open grafana at http://localhost:3000/

4. See the `Latency` dashboard: Home > Dashboards > Latency.
   Give it 5 minutes to collect enough data samples to draw meaningful graphs.

Run `docker-compose down` to stop and remove the containers.

<img width="1500" alt="image" src="https://github.com/updogliu/pyprom/assets/1288299/bf026656-02c9-427b-86ed-0e496bec1c0b">

# Grafana

http://localhost:3000/

Username: `admin`

Password: `hello`

## Persist dashboards

If you want to persist changed or new dashboard,
you can export them as JSON files (see
[here](https://grafana.com/docs/grafana/latest/dashboards/manage-dashboards/#export-and-import-dashboards)
for how to do it) into `./grafana/provisioning/dashboards` of this repo.
When the next time you create the containers, those dashboard will be already there.

# Prometheus expression browser
http://localhost:9090/graph
