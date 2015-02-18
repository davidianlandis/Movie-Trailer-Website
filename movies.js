$(function(){
	
	/* handle opening more info */
	$('.movie-tile').click(function(){
		/* remove any previous content */
		$('.movie-data').empty();
		
		
		var movieTitle = $(this).children('h2:first').html();
		var movieYear = $(this).attr('data-movie-year');
		var movieRuntime = $(this).attr('data-movie-runtime');
		var movieRated = $(this).attr('data-movie-rated');
		var movieActors = $(this).attr('data-movie-actors');
		var youtubeId = $(this).attr('data-trailer-youtube-id');
		var trailerUrl = 'http://www.youtube.com/embed/' + youtubeId + '?autoplay=1&html5=1';
		
		var imdbId = $(this).attr('data-imdb-id');
		var imdbUrl = 'http://www.imdb.com/title/'+imdbId;
		var imdbRating = $(this).attr('data-imdb-rating');
		
		var movieSynopsis = $(this).attr('data-movie-synopsis');
		var movieBoxArtUrl   = $(this).attr('data-movie-box-art-url');
		
		
		$('#movie-title').html(movieTitle);
		$('#movie-year').html(movieYear);
		$('#movie-runtime').html(movieRuntime);
		$('#movie-rated').html(movieRated);
		$('#movie-actors').html(movieActors);
		$('#movie-synopsis').html(movieSynopsis);
		$('#movie-box-art').append($('<img/>',{'src':movieBoxArtUrl,'width':'110','height':'171'}));
		$('#imdb-rating').html(imdbRating);
		$('#imdb-url').attr('href',imdbUrl);
		$('#movie-trailer').html('<iframe frameborder="no" src="'+trailerUrl+'" style="width:100%;height:100%;"></iframe>');
		
		
		
	});
	
	/* close the video if the user closes the modal */
	$('#movie-info').on('hidden.bs.modal', function () {$('#movie-trailer').empty();})

});