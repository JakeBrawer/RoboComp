
/*******************************************************************************/
/*******************************************************************************/
/*******************************************************************************/
/*******************************************************************************/
/*******************************************************************************/
/*module wheel_well(x, y, z, length, width, height)
{
    translate([x, y, z])
    cube(size = [length, width, height], center = false);
}*/
radial_precision = 200;
chassis_radius = 65;
chassis_wall_thickness   = 5;
chassis_wall_height = 44.45;
wheel_well_width = 30;
wheel_well_length = 26;
wheel_well_thickness = 4;
wire_radius = 12;

module wheel_well(){
    cube(size = [wheel_well_width, wheel_well_length, wheel_well_thickness], center = true);
}

//main body
rotate([180,0,0])
difference(){
    cylinder(r = chassis_radius, h = chassis_wall_height, $fn = radial_precision, center = true);
    //big center hole  
    translate([0, 0, -chassis_wall_thickness])
    cylinder(r=chassis_radius - chassis_wall_thickness, h=chassis_wall_height, $fn = radial_precision, center = true);
    cylinder(r = wire_radius, h = chassis_wall_height, $fn = radial_precision, center = true);
    
    translate([-(chassis_radius + chassis_wall_thickness), 0, 0])
    cube([53,/*56.5*/ 58,chassis_wall_height], true);
    //wheel wells R
    mirror([1,0,0])
    {
       translate([-(chassis_radius + chassis_wall_thickness), 0, 0])
        //translate ([-70, 0, 0])
       cube([53,/*56.5*/58,chassis_wall_height], true);
    }

}
difference(){
    translate([0, 0, -chassis_wall_height/4 + chassis_wall_thickness - 1.75])
    cube(size = [(chassis_radius - chassis_wall_thickness) * 2 - 33, 53, chassis_wall_height/2 - 2.25], center = true);
    cylinder(r = wire_radius, h = chassis_wall_height, $fn = radial_precision, center = true);
    //motor mount area 
    union(){
        //NOTE: This cube is the cutout channel for the motor mounts.
        //Width is 29mm, height is 4.5 mm, total length is 163mm.  Remember though, you
        //have the wire hole, which is 24mm across, so your length on each side is 163 - 12 = 151mm
        cube([163, 29, 4.5], true); 
        //screw hole positive
        translate([-(chassis_radius - chassis_wall_thickness*2 - 20), 5,-3]) 
        cylinder(50, 2, 2, true, $fn = radial_precision);
        mirror([1,0,0])
        {
            translate([-(chassis_radius - chassis_wall_thickness*2 - 20), 5,-3]) 
            cylinder(50, 2, 2, true, $fn = radial_precision);
        }
        //screw hole negetive
        mirror([0,1,0])
       { 
            translate([-(chassis_radius - chassis_wall_thickness*2 - 20), 5,-3]) 
        cylinder(50, 2, 2, true, $fn = radial_precision);
        mirror([1,0,0])
        {
            translate([-(chassis_radius - chassis_wall_thickness*2 - 20), 5,-3]) 
            cylinder(50, 2, 2, true, $fn = radial_precision);
        }
        }
    }
}
    
    
    //Illustration of sensor allowance
/*
    rotate([90,0,0])
    rotate([0,45,0])
    translate([0, 0, chassis_radius + chassis_wall_thickness])
    mount_IR();

    mirror(){
        rotate([90,0,0])
        rotate([0,45,0])
        translate([0, 0, chassis_radius + chassis_wall_thickness])
        mount_IR();
    }*/
   /*
     //wheel wells L
    //wheel_well(-103, -28.25, -45.675, 43, 56.5, 100);
    translate([-113, -28.25, -45.675])
    wheel_well();
    //wheel wells R
    mirror([1,0,0])
   {
       translate([-113, -28.25, -45.675])
       wheel_well();
   }
    //hole in center
    cylinder(r = wire_radius, h = chassis_wall_height, true);
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
}*/

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