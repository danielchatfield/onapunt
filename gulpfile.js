var gulp = require('gulp');
var path = require('path');
var less = require('gulp-less');
var watch = require('gulp-watch');

var paths = {
  css: ['./assets/css/**/*.less']
};

gulp.task('css', function() {
  gulp.src('./assets/css/bundle.less')
    .pipe(less())
    .pipe(gulp.dest('public/css'));
});

gulp.task('images', function(){
  gulp.src('./assets/images/**/*')
    .pipe(gulp.dest('public/images'));
});

gulp.task('watch', function() {
  gulp.watch(paths.css, ['css']);
});
