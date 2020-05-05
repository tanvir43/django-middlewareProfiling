import cProfile, pstats, StringIO

class ProfilerMiddleware(object):
	def process_request(self, request):
		prof = cProfile.Profile()
		prof.enable()
		request._prof = pr

	def process_response(self, request, response):
		request._pr.disable()
		s = StringIO.StringIO()
		sortby = 'cumulative'

		# Sort the output by cumulative time it took in fuctions.

		ps = pstats.Stats(request._pr, stream=s).sort_stats(sortby)

		# Print only 07 most time consuming functions
		ps.print_stats(7)
		print s.getvalue()
		return response
