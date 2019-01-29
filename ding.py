from waitress import serve
import server

serve(server, host='0.0.0.0', port=8080)

