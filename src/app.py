"""Flask App for metacontroller interaction for UpDownController."""
from __future__ import print_function

import logging

import updown
from flask import Flask, jsonify, request
from utils import check_exists

app = Flask(__name__)
logging.basicConfig(
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    level=logging.INFO
)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


@app.route('/sync', methods=['POST'])
def sync():
    """Sync existing and add new checks."""
    observed = request.json["parent"]
    prefix = observed.get("spec", {}).get("prefix", 'http')
    suffix = observed.get("spec", {}).get("suffix", '')
    name = observed.get("metadata", {}).get("name", False)
    url = "{}://{}/{}".format(prefix, name, suffix)

    log.info("Checking url {}".format(url))
    exists, check = check_exists(url)

    if not exists:
        log.info("Creating check on url {}".format(url))
        check = updown.add(url)

    url = observed.get("spec", {}).get("url", False)
    check.enabled = observed.get("spec", {}).get("enabled", True)
    check.period = observed.get("spec", {}).get("period", 120)
    check.apdex_t = observed.get("spec", {}).get("apdex_t", 0.25)
    check.published = observed.get("spec", {}).get("published", False)
    log.info("Syncing back to updown.io")

    return jsonify({})


@app.route('/finalize', methods=['POST'])
def finalize():
    """Delete checks in UpDown as objects are deleted in Kubernetes."""
    observed = request.json["parent"]
    prefix = observed.get("spec", {}).get("prefix", 'http')
    suffix = observed.get("spec", {}).get("suffix", '')
    name = observed.get("metadata", {}).get("name", False)
    url = "{}://{}/{}".format(prefix, name, suffix)

    exists, check = check_exists(url)
    if exists:
        deleted = check.delete()
    else:
        deleted = 'DNE'
    log.info("Delete call result {}".format(deleted))
    return jsonify({'finalized': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
