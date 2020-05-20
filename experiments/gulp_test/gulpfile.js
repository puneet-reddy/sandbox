const gulp = require('gulp');

/*
gulp.task - Define tasks
gulp.sr = Point to files to use
gulp.dest - Pointst to folder to output
gulp.watch - watch files and folders for chagnes
 */

 // Logs Message
gulp.task('message', function() {
    return console.log('Gulp is running...');
});

gulp.task('default', function() {
    return console.log('Gulp is running...');
});