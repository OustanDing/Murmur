import os, datetime, threading
from flask import *
from threading import Timer
from triangulate import *
from datetime import datetime

# Sound sample
class Sound:
	def __init__(self, vol = 0, direc = 0, time = 0):
		self.vol = vol
		self.dir = direc
		self.time = time

# Constants
UPLOAD_FOLDER = 'uploads'
x = 3 # size of grid: width
y = 3 # size of grid: height
# grid = [[1, 2, 3], [3, 2, 3], [2, 3, 1]]
grid = [Sound(13, 50, 3), Sound(14, 12, 23), Sound(150, 24, 58)]
tdelta = 5.0 # refresh delay
# for i in range(y):
# 	grid.append([])

# App initialization
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Info at one coordinate
# class Square:
# 	def __init__(self, level = 0):
# 		self.level = level

# Run a function periodically
def refresh(f, delay):
	t = Timer(delay, f)
	t.start()

def update():
	global grid
	grid = gen_random(datetime.now().strftime('%I:%M:%S%p'))
	refresh(update, tdelta)

# Upload
@app.route('/upload', methods = ['GET', 'POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']
		f.save(os.path.join(UPLOAD_FOLDER, f.filename))
	return redirect(url_for(index))

# Print info to console
def printGrid():
	global tdelta, x, y, grid
	# for i in range(x):
	# 	for j in range(y):
	# 		print(grid[i][j], end=' ')
	# 	print()
	# for i in range(x):
	# 	print('-------------------------------')
	# 	print('Volume: ' + str(grid[i].vol) + ', Direction: ' + str(grid[i].dir) + ', Time: ' + str(grid[i].time))
	# 	print('-------------------------------')
	data = exact(grid)
	print('-------------------------------')
	print('Volume: ' + str(data.vol) + ', Direction: ' + str(data.dir) + ', Time: ' + str(data.time))
	print('-------------------------------')
	# refresh(printGrid, tdelta)

# # Load index.html
# @app.route('/index', methods = ['GET'])
# def home():
# 	global grid
# 	refresh(home, tdelta)
# 	return render_template('index.html', sound=exact(grid))

# Home
@app.route('/', methods = ['GET', 'POST'])
def index():
	global grid
	update()
	printGrid()
	display = exact(grid)
	display.vol = round(display.vol, 2)
	display.dir = round(display.dir, 2)
	return render_template('index.html', sound=display)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)