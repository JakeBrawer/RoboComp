/*module wheel_well(x, y, z, length, width, height)
{
    translate([x, y, z])
    cube(size = [length, width, height], center = false);
}*/


//main body
difference(){
    cylinder(r = 105, h = 44.45, $fn = 200, center = true);
    //cylinder(44.45,77,77,true);
    difference(){
    //big center hole  
    translate([0, 0, -24.45])
    cylinder(r=95, h=44.45, $fn = 200, center = true);

    }
     //wheel wells L
    //wheel_well(-103, -28.25, -45.675, 43, 56.5, 100);
    translate([-113, -28.25, -45.675])
    cube([43,56.5,100], false);
    //wheel wells R
    mirror([1,0,0])
   {
       translate([-113, -28.25, -45.675])
    cube([43,56.5,100], false);
       }
    /*translate([60, -28.25, -45.675])
    cube([43,56.5,100], false);*/
    /* square hole in middle
    translate([0,0,-22.225])
        cube([101.6,101.6,44.45], true);
    //square extension L
    translate([-60, -25, -44.45])
    cube([55,50,50], false);
    //square extension R
    translate([5, -25, -44.45])
        cube([55,50,50], false);
    /*space for motor cord right
    translate([5, -20, -44.45])
        cube([5,40, 88.9], false);
    //space for motor cord left
    translate([-10, -20, -44.45])
        cube([5,40, 88.9], false);*/
    //another hole in the middle
    //cube([70,50,45], true);
    /*hole 1 in corner
    translate([-38, -38, 0])
        cylinder(500, 12, 12, true);
    //hole 2 in corner
    translate([-38, 38, 0])
        cylinder(500, 12, 12, true);
    //hole 3 in corner
    translate([38, -38, 0])
        cylinder(500, 12, 12, true);
    //hole 4 in corner
    translate([38, 38, 0])
        cylinder(500, 12, 12, true);*/
    //hole in center
    translate([0, 0, 0])
        cylinder(500, 12, 12, true);
    //motor mount area 
    cube([163, 29, 4.5], true); 
    //screw hole positive
    translate([-57.5, 5,-3]) 
    cylinder(50, 2, 2, true);
    mirror([1,0,0])
    {
        translate([-57.5, 5,-3]) 
    cylinder(50, 2, 2, true);
    }
    //screw hole negetive
    mirror([0,1,0])
   { 
    mirror([1,0,0])
    {
        translate([-57.5, 5,-3]) 
    cylinder(50, 2, 2, true);
    }
}
    mirror([0,1,0])
    {
        translate([-57.5, 5,-3]) 
    cylinder(50, 2, 2, true);
    }
}

/*controller
    translate([0,0,44.45])
        cube([101.6,101.6,44.45], true);*/
/*camera
translate([0,76.8,44.45])
        cylinder(r=26, h=44.45, $fn = 200, center = true);*/
/*main motor left
rotate([0,90,0])
    translate([15, 0, -38.5])
cylinder(43, 7, 7, true);
//main motor right
rotate([0,90,0])
    translate([15, 0, 38.5])
cylinder(43, 7, 7, true);*/
