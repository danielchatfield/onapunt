var gulp = require('gulp');
var path = require('path');
var less = require('gulp-less');
var watch = require('gulp-watch');

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
