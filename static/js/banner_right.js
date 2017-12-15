(function ($) {
    $(function () {
        var $sideroll       = $("#sideroll"), // айди блока который будет появляться
            $watch_block    = $("#sideroll"),  // айди блока положение которого отслеживается

            enabled         = true,
            hide_offset     = 5,
            outer_margin    = 10,
            shown           = false,

            show = function() {
                if(shown) return;
                shown = true;

                $sideroll.stop().animate({right: -hide_offset}, 300);
            },

            hide = function() {
                if(!shown) return;
                shown = false;

                $sideroll.stop().animate({right: -$sideroll.outerWidth()-outer_margin}, 300);
            },

            disable = function(e) {
                e.preventDefault();
                enabled = false;
                hide();
            },

            onscroll = function() {
                if(!enabled) return;

                var viewport_bottom = $(window).scrollTop() + $(window).height(),
                    block_bottom    = $watch_block.offset().top + $watch_block.outerHeight();

                if(viewport_bottom > block_bottom)
                    show()
                else
                    hide();
            };

        $(".roll-close", $sideroll).click(disable);

        $(window).scroll(onscroll).resize(onscroll);
    })
})(jQuery);