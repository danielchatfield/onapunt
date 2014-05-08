var gulp = require('gulp');
var path = require('path');
var less = require('gulp-less');
var watch = require('gulp-watch');

/*
  This is the task runner used to compile the assets. It does the following:
   - compiles and concatenates less files
   - copies images
   - copies fonts
   - watches for changes and recompiles


  Some things it will do:
   - clean build directory before copying compiled assets
   - compress images
   - compile js (not sure whether will use coffeescript yet)
   - compile jinja templates down to byte code
   - catch stream errors properly

  We don't need to worry about inlining images or anything like that as Google
  App Engine supports the SPDY protocol extension which removes almost all of
  the overhead associated with multiple requests.

*/

var paths = {
  css: ['./assets/css/**/*.less'],
  images: ['./assets/images/**/*'],
  fonts: ['./assets/fonts/**/*']
};

gulp.task('css', function() {
  gulp.src('./assets/css/bundle.less')
    .pipe(less())
    .pipe(gulp.dest('public/css'));
});

gulp.task('fonts', function(){
  gulp.src(paths.fonts)
    .pipe(gulp.dest('public/fonts'));
});


gulp.task('images', function(){
  gulp.src(paths.images)
    .pipe(gulp.dest('public/images'));
});

gulp.task('watch', function() {
  gulp.watch(paths.css, ['css']);
  gulp.watch(paths.images, ['images']);
});


gulp.task('build', ['css', 'images', 'fonts']);

gulp.task('default', ['build', 'watch']);
