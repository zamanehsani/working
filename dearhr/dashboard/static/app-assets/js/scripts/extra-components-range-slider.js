/*
 * Range Slider - Extra Components
 */

$(function() {
	//Start without params


	//Set up range with negative values

	//Set up range with fractional values, using fractional step


	//One more example with strings
	$("#range_09").ionRangeSlider({
		type: "double",
		grid: true,
		drag_interval: false,
		from_fixed: true,
		hide_min_max: true,
		to_fixed: true,
		from: 3,
		to: 5,
	    values: ["300","4000","5000", "avg", "7000","8000", "9000" ]
	});
});