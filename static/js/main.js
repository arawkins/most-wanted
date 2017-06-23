$(document).foundation();

// Class to represent a row in the seat reservations grid

var model = {
    activeClient: ko.observable(''),
    state: ko.observable('list'),
    clients: [
        {'name':'Client A', 'value':'client_a'},
        {'name':'Client B', 'value':'client_b'},
        {'name':'Client C', 'value':'client_c'}
    ],
    product_areas: ['Billing', 'Policies', 'Claims', 'Reports'],
    featureRequests: ko.observableArray([]),
    changeState: function(newState) {
        if (newState == 'list' || newState == 'create') {
            this.state(newState);
            if (this.state() == 'list') {
                var current_client = $("#client_selector").val();
            }
        } else {
            console.log("invalid state " + newState);
        }
    },
    getActiveClientData: function() {
        var self = this;
        if (self.activeClient() != '') {
            $.get( "get/"+self.activeClient(), function( data ) {
                self.featureRequests(data);
            });
        }
    }
};

ko.applyBindings(model);

$('#client_selector').change(function(e) {
    if (e.target.value != undefined && e.target.value != '') {

        $.get( "get/"+e.target.value, function( data ) {
            model.featureRequests(data);
        });
    } else {
        model.featureRequests([]);
    }
});

$("#new_request_form form").submit(function(e) {
    $.post('/create/', $(this).serialize(), function(data) {
        model.getActiveClientData();
        model.changeState('list');
    });
    e.preventDefault();
});

$(function(){
	$('#target_date').fdatepicker({
		format: 'mm-dd-yyyy',
		disableDblClickSelection: true,
		leftArrow:'<<',
		rightArrow:'>>',
		closeIcon:'X',
		closeButton: true
	});
});
