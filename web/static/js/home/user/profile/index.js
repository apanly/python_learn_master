;
var profile_index_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        var that = this;
        $(".set_info").click( function(){
            common_ops.popLayer( home_common_ops.buildUrl("/profile/set_info") );
        } );
    }
};
$(document).ready(function () {
    profile_index_ops.init();
});