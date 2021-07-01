/*FormWizard Init*/
$(function(){
	"use strict";
	
	/* Basic Wizard Init*/
	if($('#example-basic').length >0)
		$("#example-basic").steps({
			headerTag: "h3",
			bodyTag: "section",
			transitionEffect: "fade",
			autoFocus: true,
			titleTemplate: '<span class="number">#index#</span> #title#',
		});

	if($('#example-advanced-form').length >0){
		var form_2 = $("#example-advanced-form");
		form_2.steps({
			headerTag: "h3",
			bodyTag: "fieldset",
			transitionEffect: "fade",
			titleTemplate: '#title#',
			labels: {
				finish: "place order",
				next: "Next",
				previous: "Previous",
			},
			onStepChanging: function (event, currentindex, newindex)
			{
				// Allways allow previous action even if the current form is not valid!
				if (currentindex > newindex)
				{
					return true;
				}
				// Forbid next action on "Warning" step if the user is to young
				if (newindex === 3 && Number($("#age-2").val()) < 18)
				{
					return false;
				}
				// Needed in some cases if the user went back (clean up)
				if (currentindex < newindex)
				{
					// To remove error styles
					form_2.find(".body:eq(" + newindex + ") label.error").remove();
					form_2.find(".body:eq(" + newindex + ") .error").removeClass("error");
				}
				form_2.validate().settings.ignore = ":disabled,:hidden";
				return form_2.valid();
			},
			onFinishing: function (event, currentindex)
			{
				form_2.validate().settings.ignore = ":disabled";
				return form_2.valid();
			},
			onFinished: function (event, currentindex)
			{
				alert("Submitted!");
			}
		}).validate({
			errorPlacement: function errorPlacement(error, element) { element.before(error); },
			rules: {
				confirm: {
					equdelo: "#password-2"
				}
			}
		});
	}
	
	$('#datable_1').DataTable({
		 "bFilter": false,
		 "bLengthChange": false,
		 "bPaginate": false,
		 "bInfo": false,
		  "footerCallback": function ( row, data, start, end, display ) {
				var api = this.api(), data;
	 
				// Remove the formatting to get integer data for summation
				var intVal = function ( i ) {
					return typeof i === 'string' ?
						i.replace(/[\$,]/g, '')*1 :
						typeof i === 'number' ?
							i : 0;
				};
	 
				// Total over all pages
				var total = api
					.column( 3 )
					.data()
					.reduce( function (a, b) {
						return intVal(a) + intVal(b);
					}, 0 );
	 
				// Total over this page
				var pageTotal = api
					.column( 3, { page: 'current'} )
					.data()
					.reduce( function (a, b) {
						return intVal(a) + intVal(b);
					}, 0 );
	 
				// Update footer
				$( api.column( 3 ).footer() ).html(
					'$'+pageTotal
				);
			}
	});
	
});
		