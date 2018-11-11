if (typeof(Example) == "undefined") {
    var Example = {};
}

(function ($) {
    Example.Modal = function() {
        this.initialize.apply(this, arguments);
    };
}

Example.Modal.prototype = {
    initialize : function (hash) {
        var obj = this;

        this.hash = this.getHashData(hash);
        
    }
};

);