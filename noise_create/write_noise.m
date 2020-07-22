[M,N] = size(Z_star);
file = fopen('F:\Matlab2015a\bin\501\pid_filter\nstar0.txt', 'wt');
for i=1:N
    fprintf(file, '%.30f\n', Z_star(1,i));
end
fclose(file);
file = fopen('F:\Matlab2015a\bin\501\pid_filter\nstar1.txt', 'wt');
for i=1:N
    fprintf(file, '%.30f\n', Z_star(2,i));
end
fclose(file);
file = fopen('F:\Matlab2015a\bin\501\pid_filter\nstar2.txt', 'wt');
for i=1:N
    fprintf(file, '%.30f\n', Z_star(3,i));
end
fclose(file);
file = fopen('F:\Matlab2015a\bin\501\pid_filter\nstar3.txt', 'wt');
for i=1:N
    fprintf(file, '%.30f\n', Z_star(4,i));
end
fclose(file);
file = fopen('F:\Matlab2015a\bin\501\pid_filter\ngyroPhi.txt', 'wt');
for i=1:N
    fprintf(file, '%.30f\n', Z_gyro(1,i));
end
fclose(file);
file = fopen('F:\Matlab2015a\bin\501\pid_filter\ngyroTheta.txt', 'wt');
for i=1:N
    fprintf(file, '%.30f\n', Z_gyro(2,i));
end
fclose(file);
file = fopen('F:\Matlab2015a\bin\501\pid_filter\ngyroPsi.txt', 'wt');
for i=1:N
    fprintf(file, '%.30f\n', Z_gyro(3,i));
end
fclose(file);