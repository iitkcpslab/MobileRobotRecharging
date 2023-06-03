clear all;
close all;
dim_x = 17; dim_y = 17;
axis([-1 dim_x -1 dim_y]);
rectangle('Position', [0, 0, 17, 17], 'linewidth',2);
for i=0:16
        rectangle('Position', [0, i, 17, 1]);
end

for i=0:16
        rectangle('Position', [i, 0, 1, 17]);
end

rectangle('Position',[9, 1, 1, 1], 'facecolor', 'black');
rectangle('Position',[9, 2, 1, 1], 'facecolor', 'black');
rectangle('Position',[3, 3, 1, 1], 'facecolor', 'black');
rectangle('Position',[9, 3, 1, 1], 'facecolor', 'black');
rectangle('Position',[3, 4, 1, 1], 'facecolor', 'black');
rectangle('Position',[5, 4, 1, 1], 'facecolor', 'black');
rectangle('Position',[6, 4, 1, 1], 'facecolor', 'black');
rectangle('Position',[7, 4, 1, 1], 'facecolor', 'black');
rectangle('Position',[9, 4, 1, 1], 'facecolor', 'black');
rectangle('Position',[10, 4, 1, 1], 'facecolor', 'black');
rectangle('Position',[11, 4, 1, 1], 'facecolor', 'black');
rectangle('Position',[14, 4, 1, 1], 'facecolor', 'black');
rectangle('Position',[15, 4, 1, 1], 'facecolor', 'black');
rectangle('Position',[1, 5, 1, 1], 'facecolor', 'black');
rectangle('Position',[2, 5, 1, 1], 'facecolor', 'black');
rectangle('Position',[3, 5, 1, 1], 'facecolor', 'black');
rectangle('Position',[11, 5, 1, 1], 'facecolor', 'black');
rectangle('Position',[11, 6, 1, 1], 'facecolor', 'black');
rectangle('Position',[6, 8, 1, 1], 'facecolor', 'black');
rectangle('Position',[7, 8, 1, 1], 'facecolor', 'black');
rectangle('Position',[8, 8, 1, 1], 'facecolor', 'black');
rectangle('Position',[15, 8, 1, 1], 'facecolor', 'black');
rectangle('Position',[6, 9, 1, 1], 'facecolor', 'black');
rectangle('Position',[8, 9, 1, 1], 'facecolor', 'black');
rectangle('Position',[14, 9, 1, 1], 'facecolor', 'black');
rectangle('Position',[6, 10, 1, 1], 'facecolor', 'black');
rectangle('Position',[8, 10, 1, 1], 'facecolor', 'black');
rectangle('Position',[13, 10, 1, 1], 'facecolor', 'black');
rectangle('Position',[1, 12, 1, 1], 'facecolor', 'black');
rectangle('Position',[2, 12, 1, 1], 'facecolor', 'black');
rectangle('Position',[3, 12, 1, 1], 'facecolor', 'black');
rectangle('Position',[10, 13, 1, 1], 'facecolor', 'black');
rectangle('Position',[9, 14, 1, 1], 'facecolor', 'black');
rectangle('Position',[8, 15, 1, 1], 'facecolor', 'black');


hold on;
