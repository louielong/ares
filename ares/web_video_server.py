#!/usr/bin/env python 
# -*- coding=utf-8 -*-

import tornado.web
import tornado.ioloop
import os

video_dir = os.path.dirname(__file__)+'videos'

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		video_files = [unicode(f, "UTF-8") for f in os.listdir(video_dir) if f.endswith('mp4')]
		video_files_number = len(video_files)
		self.set_header('Accept-Ranges', 'bytes')
		if video_files_number is 0:
			self.write('No mp4 file found, directory empty!')
		else:
			self.render('index.html',
					title = 'home',
					info = 'Welcom to Web Video Server',
					video_files_number = video_files_number,
					video_files = video_files
					)

class VideoHandler(tornado.web.RequestHandler):
	def get(self, filename):
		self.set_header('Accept-Ranges', 'bytes')
		self.render('play.html',
			title = filename,
			video_file = filename
		)

if __name__ == '__main__':
	app = tornado.web.Application(
		[
		(r"/", MainHandler),
		(r"/video/(.*)", VideoHandler),
		],
		template_path = os.path.join(os.path.dirname(__file__), "templates"),
		debug=True
		)
	app.listen(8000)
	tornado.ioloop.IOLoop.current().start()
