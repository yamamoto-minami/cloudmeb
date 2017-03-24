$.fn.serializeObject = function(useId) {
    var $form = this,
        obj = {};

    $.each($form.serializeArray(), function() {
        var prop = useId ? 
            $form.find(['[name="', '"]'].join(this.name)).attr('id') 
            : this.name;

        if (obj[prop] !== undefined) {
            if (!obj[prop].push) {
                obj[prop] = [obj[prop]];
            }
            obj[prop].push(this.value || '');
        } else {
            obj[prop] = this.value || '';
        }
    });

    return obj;
};

$.fn.inView = function() {
    var height = this.height(),
        rect = this.get(0)
        .getBoundingClientRect();

    return (rect.top >= -height && rect.bottom <= (window.innerHeight + height || 
        document.documentElement.clientHeight + height));
};

$(document).ready(function(e) {

    function getPrice(formula, context) {
        return eval(Object.prototype.toString.call(context) === '[object Object]' ?
            formula.replace(/%\(\w+\)s/g, function(match) {
                return String(context[match.slice(2, -2)]);
            }) : null);
    }

    function trackEvent(category, action, label, value) {
        label = [category, action, label].join('-');
        _gaq.push(['_trackEvent', category, action, label, value]);
    }

    function growl(html, type, dismissible, animation, timout) {
        // Usage:
        // growl('<strong>Info!</strong> Product added', 'info', true);
        var timer,
            counter = timout || 5,
            $close = $('<button />', {
                'type': 'button',
                'class': 'close',
                'data-dismiss': 'alert',
                'aria-label': gettext('Close')
            }).append($('<span />', {
                'area-hidden': true
            }))
            .html('&times;'),
            $growl = $('<div />', {
            'role': 'alert',
            'class': [
                'alert', 
                ['alert', type].join('-'), 
                dismissible ? 'alert-dismissible' : '',
                'fade',
                'in',
                'animated',
                animation || 'bounceInDown'
            ].join(' ')
        })
        .html(html);

        dismissible && $growl.prepend($close);

        $('.growl').append($growl);

        timer = setInterval(function() {
           !$growl.is(':hover') && counter--;
           if (counter == 0) {
                $growl.animate({'opacity': 0}, {
                    duration: 500,
                    complete: function() {
                        $growl.alert('close');
                    }
                });
                clearInterval(timer);
           }
        }, 1000);

        $growl.on('mouseout', function(e) {
            counter = 5;
        });

        return $growl;
    }

    // window.growl = growl;

    // function disabelAddThisHover() {
    //     var $btn = $('.addthis_button_more');
    //     if ($btn.length) {
    //         $btn.on('hover click', function(e) {
    //             e.stopPropagation();
    //             e.stopImmediatePropagation();
    //         });
    //     } else {
    //         setTimeout(disabelAddThisHover, 500);
    //     }
    // }

    // disabelAddThisHover();

    $('a[data-lang]').click(function(e) {
        e.stopImmediatePropagation();
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/i18n/setlang/',
            data: {
                language: $(e.currentTarget).data('lang'),
                next: '/'
            },
            beforeSend: function(request) {
                request.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
            }
        })
        .done(function(response) {
            location.href = $('link[rel="alternate"]').attr('href');
            // Need to fix query to try both languages.
            // location.reload();
        });
    });

    $('.navbar-toggle').on('click', function() {
        var $this = $(this),
            isExpanded = $this.attr('aria-expanded') == 'false';

        $('html').css('overflow', isExpanded ? 'hidden' : '');

        if (isExpanded) {
            $this.closest('.navbar').addClass('navbar-default');
        } else {
            setTimeout(function(e) {
                $(document).trigger('scroll');
             }, 0);
        }
    });

    $(window).on('scroll', function(e) {
        $('[data-animate-on-scroll="true"]').each(function(item, index) {
            var $this = $(this),
                classes = ['animated', $this.data('animation-name')].join(' ');

            $this[$this.inView() ? 'addClass' : 'removeClass'](classes);
        });
    });

    (function() {
        var $addons = $('.before .addons, .after .addons')
            .each(function(index, item) {
                var $this = $(this);
                setTimeout(function() {
                    $this.width($this.parent().width());
                }, 500);
            });


        if ($addons.length) {
            setInterval(function() {
                var $beforeAddons = $('.before .addons'),
                    $beforeParent = $beforeAddons.parent(),
                    $afterAddons = $('.after .addons'),
                    $afterParent = $afterAddons.parent(),
                    beforePosition = $beforeAddons.filter('.active').index() - 2, // This is the number of non addon items (a)
                    afterPosition = $afterAddons.filter('.active').index() - 2, // This is the number of non addon items (a)
                    nextBeforePosition = beforePosition == $beforeAddons.length - 1 ? 0 : beforePosition + 1,
                    nextAfterPosition = afterPosition == $afterAddons.length - 1 ? 0 : afterPosition + 1;


                if ($beforeParent.hasClass('expanded') || $afterParent.hasClass('expanded')) {
                    return;
                }

                if (!$beforeParent.parent().is(':hover') || !$afterParent.parent().is(':hover')) {
                    $beforeAddons
                        .width($beforeParent.width())
                        .removeClass('active')
                        .eq(nextBeforePosition)
                        .addClass('active');

                    $afterAddons
                        .width($afterParent.width())
                        .removeClass('active')
                        .eq(nextAfterPosition)
                        .addClass('active');
                }
            }, 3000);
        }
    })();

    $('.before-after > div > div').on('click', function(e) {
        var $this = $(this),
            $clone = $this.clone(),
            position = $this.position(),
            css = {
                'position': 'absolute',
                'z-index': '100',
                'width': '50%',
                'opacity': '0'
            };

        if ($(window).width() < 992) {
            css[$this.hasClass('before') ? 'left' : 'right'] = 0;

            $this
                .after(
                    $clone
                        .addClass('expanded')
                        .css(css)
                        .animate({
                            'width': '100%',
                            'opacity': '1'
                        }, {
                            duration: 500,
                            start: function(e) {
                                $(this).find('li').css('opacity', '0');
                            },
                            complete: function(e) {
                                $(this).find('li').animate({'opacity': '1'}, 500);
                            } 
                        })
                        //.find('.close-btn')
                        .on('click', function($clone, e) {
                            $clone
                                .find('li')
                                .animate({'opacity': '0'}, {
                                    duration: 500,
                                    complete: function(e) {
                                        $clone.animate({
                                            'width': '50%',
                                            'opacity': '0'
                                        }, {
                                            duration: 500,
                                            complete: function(e) {
                                                $clone.remove();
                                            } 
                                        });
                                    }
                                });
                        }.bind(null, $clone))
                        //.end()
                        .find('.addons')
                        .hide()
                        .filter('.active')
                        .show()
                        .css({
                            'width': '100%',
                            'opacity': '1'
                        })
                        .end()
                        .end()
                );
        }
    });

    $(window).on('resize', function(e) {
        var $beforeAfter = $('.before-after > div > div'),
            padding = $(window).width() > 1600 ? '20%' : $beforeAfter.css('paddingRight');

        $beforeAfter.each(function(item, index) {
            var $this = $(this),
                isBefore = $this.hasClass('before');

            $this.css(isBefore ? 'padding-left' : 'padding-right', padding);
        });
    });

    $(window)
        .on('scroll resize', function(e) {
            var $window = $(this),
                $document = $(document),
                $nav = $('.navbar-scroll'),
                $hero = $('.hero-unit'),
                $lead = $hero.find('.lead'),
                $steps = $('.configurator-steps > *'),
                $container = $hero.next('.container-fluid'),
                scrollTop = $window.scrollTop(),
                hasNoScroll = $window.height() == $document.height(),
                isContainerAtTop = $container.length && $container.get(0).getBoundingClientRect().top > 0,
                isScrollAtBottom = scrollTop + $window.height() == $document.height(),
                margin = ['-', 'px'].join(scrollTop),
                leadScale = ['scale(', ')'].join((100 - (scrollTop / 10)) / 100),
                stepsScale = ['scale(', ')'].join((100 - (scrollTop / 2)) / 100),
                leadOpacity = (100 - (scrollTop / 5)) / 100,
                stepsOpacity = (100 - (scrollTop * 1.5)) / 100;

            !$nav.find('[aria-expanded="true"]').length && $nav[scrollTop > 0 ? 'addClass' : 'removeClass']('navbar-default');

            if ($window.width() < 760) {
                return;
            }

            // if there is no scroll bar we need to reset the margin.
            if (hasNoScroll || isContainerAtTop && !isScrollAtBottom) {
                $container.css('margin-top', margin);
                
                $lead.css({
                    'opacity': leadOpacity,
                    'transform': leadScale
                });

                $steps
                    .css('opacity', stepsOpacity)
                    .filter('h1').css('transform', stepsScale);
            }
        })
        .trigger('scroll');

    // Make footer sticky if the document height is smaller than the window height.
    function positionFooter(e) {
        $('footer')
            .attr('style', '')
            .css({
                position: $(document).height() > $(window).height() ? 'relative' : 'absolute',
                bottom: 0,
                visibility: 'visible'
            });
    }

    // Ensure that the modals are centered on the page.
    function positionModals(e) {
        var $this = $(this).css('display', 'block'),
            $window = $(window),
            $dialog = $this.find('.modal-dialog'),
            // offset = Math.abs(($window.height() - $window.scrollTop() - $dialog.height()) / 2),
            offset =($window.height() - $dialog.height()) / 2,
            marginBottom = parseInt($dialog.css('margin-bottom'), 10);

        $dialog.css('margin-top', offset < marginBottom ? marginBottom : offset);
    }

    $(document).on('show.bs.modal', '.modal', positionModals);

    $(window).on('resize', function() {
        $('.modal:visible').each(positionModals);
    });

    $('.configurator-steps li, .faq .panel-heading').on('click', function(e) {
        setTimeout(positionFooter, 500);
    });


    $(window).load(function(e) {
        $(this)
            .on('resize', positionFooter)
            .trigger('resize');
    });

    $('[data-toggle="btns"] .btn').on('click', function(e) {
        var $this = $(this);

        if (history.pushState) {
            history.pushState(null, null, $this.attr('href'));
        } else {
            location.hash = $this.attr('href');
        }

        $this
            .parent()
            .find('.active')
            .removeClass('active');

        $this.addClass('active');

        // Reset the filter
        $('.solutions-filter input')
            .val('')
            .trigger('blur');

        // Hide the no result msg
        $('.solutions-filter-empty').hide();
        
        paginator();

        _gaq.push(['_trackPageview', location.pathname + location.search + location.hash]);
    });

    $('#testemonial-carousel')
        .owlCarousel({
            autoplay : true,
            dots: false,
            autoplaySpeed: 1500,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            margin: 30,
            autoWidth: true,
            autoHeight: true,
            items: 3,
            center: true,
            loop: true
        })
        .on('translate.owl.carousel', function(e) {
            $(this)
                .find('.flip')
                .removeClass('current')
                .removeClass('flipped')
                .find('> img[data-toggle="tooltip"]')
                .data('placement', 'right');
        })
        .on('translated.owl.carousel', function(e) {
            $(this)
                .find('.flip')
                .eq(e.item.index)
                .addClass('current');
        })
        .on('click', '.flip', function() {
            var $this = $(this),
                index = parseInt($this.data('index'));

            if ($this.hasClass('current')) {
                $this
                    .toggleClass('flipped')
                    .find('> img[data-toggle="tooltip"]')
                    .data('placement', 'left');
            } else {
                $this
                    .closest('#testemonial-carousel')
                    .trigger('to.owl.carousel', [index, 500, true])
            }
        });

    $('#partner-carousel').owlCarousel({
        autoplay : true,
        dots: false,
        autoWidth: true,
        autoHeight: false,
        autoplaySpeed: 1000,
        autoplayTimeout: 1500,
        autoplayHoverPause: true,
        margin: 30,
        loop: true,
        center: true,
        items: $('#partner-carousel img').length
    });

    $('.category-carousel')
        .owlCarousel({
            autoplay : false,
            dots: false,
            margin: 0,
            loop: true,
            center: true,
            items: 5,
            responsive: {
                0: {
                    items: 1
                },
                // 768: {
                //     items: 2
                // },
                992: {
                    items: 3
                },
                1200: {
                    items: 5
                }
            }
        })
        .on('click', '.owl-item a', function(e) {
            // var $this = $(this),
            //     index = parseInt($this.data('index'));

            // $this
            //     .closest('.category-carousel')
            //     .trigger('to.owl.carousel', [index, 250, true]);


            // As per Adrian's comment
            $(this)
                .closest('.category-carousel')
                .find('a')
                .removeClass('active')
                .end()
                .end()
                .addClass('active');
        })
        .on('translated.owl.carousel', function(e) {
            $(this)
                .find('a')
                .filter('.active')
                .removeClass('active')
                .end()
                .eq(e.item.index)
                .trigger('click')
                .addClass('active');
        });

    $('.category-carousel-wrapper [data-direction]').on('click', function(e) {
        // var $this = $(this);

        // $this
        //     .parent()
        //     .find('.category-carousel')
        //     .trigger([$this.data('direction'), 'owl', 'carousel'].join('.'));

        // As per Adrian's comment
        var $this = $(this),
            $carousel = $this.parent().find('.category-carousel'),
            index = $carousel.find('a.active').data('index');

        $carousel.trigger('to.owl.carousel', [$this.data('direction') == 'next' ? index + 1 : index - 1, 250, true]);


    });

    function refreshCategoryCarousel(isProduct) {
        var $carousel = $(['.category-carousel', isProduct ? 'products' : 'services'].join('.')),
            carousel = $carousel.data('owlCarousel');

        $carousel.css('opacity', 0);

        setTimeout(function() {
            carousel._width = $carousel.width();
            carousel.invalidate('width');
            carousel.refresh();
            $carousel.css('opacity', 1);
        }, 500);
    }

    var paginateBy = 9,
        paginatorInitialized = false;

    $('.pagination').on('click', function(e) {
        e.preventDefault();

        var range, index,
            $currentItem = $(e.target).closest('li'),
            $items = $currentItem.closest('.pagination').find('li.pagination-item'),
            $targetItem = $currentItem.hasClass('pagination-item') ?
                $currentItem : $currentItem.hasClass('next') ?
                $items.filter('.active').next().length ? 
                $items.filter('.active').next() : $items.eq(0) : $items.filter('.active').prev();

        index = $targetItem.index();

        index < 1 || index > $items.length && $targetItem.addClass('disabled');

        if (!$targetItem.hasClass('disabled')) {
            range = {
                from: index * paginateBy + 1 - paginateBy,
                to: index * paginateBy
            };

            $items.removeClass('active');

            $targetItem
                .addClass('active')
                .closest('.tab-pane')
                .find('.solutions-item')
                .not('.filtered')
                .each(function(index, item) {
                    $(this)[index + 1 >= range.from && index + 1 <= range.to ? 'show' : 'hide']();
                });

            if (e.originalEvent) {
                window.scrollTo(0, 0);
                $('html, body').animate({
                    scrollTop: $targetItem.closest('.container-fluid').offset().top - 10
                }, 1000);
            } else {
                !paginatorInitialized && setTimeout(function() {
                    window.scrollTo(0, 0);
                }, 0);
            }
        }
    });

    function paginator() {
        $.each([
            {
                length: Math.ceil($(['#', ' .solutions-item'].join(gettext('products'))).not('.filtered').length / paginateBy),
                $paginator: $(['#', ' .pagination'].join(gettext('products')))
            },
            {
                length: Math.ceil($(['#', ' .solutions-item'].join(gettext('services'))).not('.filtered').length / paginateBy),
                $paginator: $(['#', ' .pagination'].join(gettext('services')))
            }
        ], function(index, item) {
            var $items = [];

            for (var i = 0; i < this.length; i++) {
                $items.push($('<li />', {
                    'class': 'pagination-item'
                }).html($('<a />', {
                    href: ['#', this.$paginator.closest('.tab-pane').attr('id')].join('')
                }).text(i + 1)));
            }

            this.$paginator[this.length > 1 ? 'show' : 'hide']();
            this.$paginator.find('li.pagination-item').remove();
            this.$paginator.find('li').first().after($items);
            this.$paginator.find('li.pagination-item').first().click();
        });

        paginatorInitialized = true;
    }

    function highlight(node, str) {
        var re = new RegExp(['(', ')(?![^<]*>|[^<]*<\/>)'].join(str), 'gi'),
            originalHTML = node.originalHTML = node.originalHTML || node.innerHTML;

        node.innerHTML = str ? originalHTML.replace(re, function(str) {
            return ['<span class="highlight">', '</span>'].join(str);
        }) : originalHTML;
    }

    function filterSolutions(value) {
        var $solutions = $('.active .solutions-item')
            .attr('style', '');

        $solutions.each(function(index, item) {
            var $this = $(this),
                matched = false,
                contents = [
                    $this.find('h4'),
                    $this.find('h5'),
                    $this.find('p')
                ];

            $.each(contents, function(index, item) {
                matched = matched || this.text().match(new RegExp(value, 'gi'));
                matched && highlight(this.get(0), value);
            });

            $this[matched ? 'removeClass' : 'addClass']('filtered');
            setTimeout(paginator, 0);
        });

        $('.solutions-filter-empty')
            .find('span')
            .text(['"', '"'].join(value))
            .end()
            [$solutions.filter(':visible').length ? 'hide' : 'show']();

        $(window).trigger('resize');
    }

    $('.solutions-filter button').on('click', function(e) {
        filterSolutions($(this).closest('.solutions-filter').find('input').val().trim());
    });

    $('.solutions-filter input').on('blur', function(e) {
        filterSolutions($(this).val().trim());
    });

    $('.solutions-filter input').on('keyup', function(e) {
        e.which == 13 && $(this).blur();
    });

    // $('.solutions-filter input').on('keyup keypress', function(e) {
    //     filterSolutions($(this).val().trim());
    // });

    function showHideEmptyMsg(isProduct) {
        var className = isProduct ? 'products' : 'services',
            $solutionsRow = $(['.configurator-solutions-wrapper', className].join(' .')),
            isEmpty = $solutionsRow
                .find('[data-solution-id]')
                .parent()
                .not('.hidden')
                .length < 1;

        $solutionsRow
            .find('.empty')
            [isEmpty ? 'removeClass' : 'addClass']('hidden');

        $(['.configurator-solutions-basket', className].join(' .'))
            .find('.empty')
            [isEmpty ? 'removeClass' : 'addClass']('hidden');

        // Should be elsewhere it's just handy like this ;)
        // Reposition footer.
        $(window).trigger('resize');
    }

    function calculatePriceBuckets() {
        var prices = {},
            ids = {},
            $priceTotals = $('.pricing-totals'),
            $form = $('form.user-info');

        $('.configurator-solutions-basket [data-solution-id]')
            .not('.hidden')
            .find('.price')
            .each(function(index, item) {
                var $this = $(this),
                    price = prices[$this.data('price-frequency')];

                prices[$this.data('price-frequency')] = (price || 0) + parseInt($this.find('span').text().replace(',', ''));
                ids[$this.data('price-frequency')] = $this.data('price-frequency-id');
            });

        $priceTotals
            .find('[data-price]')
            .remove();

        for (var price in prices) {
            $priceTotals
                .find('.btn')
                .before($('<h4 />', {
                    'data-price': parseFloat(prices[price]).toLocaleString(),
                    'data-price-id': ids[price]
                }).text(price));
        }

        $priceTotals
            .find('[data-price-id]')
            .each(function(item, index) {
                var $this = $(this);

                $form
                    .find(['#', ' input'].join($this.data('price-id')))
                    .val(parseFloat(String($this.data('price')).replace(',', '')));
        });
    }

    function calculatePrice() {
        $('[data-pricing-formula]').each(function(index, item) {
            var price = 0,
                $solution = $(this),
                $basketSolution = $(['.configurator-solutions-basket [data-solution-id="', '"]']
                    .join($solution.data('solution-id'))
                ),
                $addMoreSolution = $(['.add-more-modal [data-solution-id="', '"]']
                    .join($solution.data('solution-id'))
                ),
                $swapSolution = $(['.swap-modal [data-solution-id="', '"]']
                    .join($solution.data('solution-id'))
                );

            price = parseFloat(getPrice(String($solution.data('pricing-formula')), 
                $solution.find('form').serializeObject()
            )).toLocaleString();

            $basketSolution
                .find('.price span')
                .text(price);

            $addMoreSolution
                .find('.price span')
                .text(price);

            $swapSolution
                .find('.price span')
                .text(price);

            $solution
                .find('.price span')
                .text(price);
        });
    }

    function selectSolutions() {
        var $form = $('form.user-info'),
            solutions = {
                products: [],
                services: []
            };

        $('.configurator-solutions-basket [data-solution-id]')
            .not('.hidden')
            .each(function(item, index) {
                var $this = $(this),
                    value = $form
                        .find(['[data-value-id="', '"]'].join($this.data('solution-id')))
                        .val();

                solutions[$(this).hasClass('product') ? 'products' : 'services'].push(value);
            });

        for (var prop in solutions) {
            $form
                .find(['.', ' .selectpicker'].join(prop))
                .selectpicker('val', solutions[prop]);
        }
    }

    function selectCategories() {
        var $form = $('form.user-info'),
            categories = [];

        $('.configurator-solutions-basket [data-solution-id]')
            .not('.hidden')
            .each(function(item, index) {
                var $this = $(this);

                $.each($this.data('categories-id'), function(index, item) {
                    if ($.inArray(this, categories) == -1) {
                        categories.push(this);
                    }
                });
            });

        $form
            .find('.categories .selectpicker')
            .selectpicker('val', categories);
    }

    function getSolutionsConfiguration() {
        var $form = $('form.user-info'),
            solutions = {
                products: [],
                services: []
            };

        $('.configurator-solutions-basket [data-solution-id]')
            .not('.hidden')
            .each(function(item, index) {
                var $this = $(this),
                    data = $([
                        '.configurator-solutions [data-solution-id="', 
                        '"] form'
                    ].join($this.data('solution-id')))
                    .serializeObject();

                data.name = $this.find('h4').text();
                solutions[$(this).hasClass('product') ? 'products' : 'services'].push(data);
            });

         for (var prop in solutions) {
            $form
                .find(['.', '-configuration textarea'].join(prop))
                .val(JSON.stringify(solutions[prop], null, 4));
        }
    }

    function propegateDisplayValue($this, $inputs) {
        var value = $this.attr('type') == 'radio' ?
            $this.closest('.form-group').find(':checked').val() :
            $this.val();

        $inputs.closest('[data-solution-id]')
            .find(['[data-value-input-id="', '"]'].join($this.data('input-id')))
            .text(value);
    }

    function propegateValue($this, $inputs) {
        if ($this.hasClass('selectpicker')) {
            $inputs.selectpicker('val', $this.selectpicker('val'));
        } else if ($this.attr('type') == 'radio') {
            $this.prop('checked') && $inputs.filter(['[value="', '"]'].join($this.val())).prop('checked', $this.prop('checked'));
        } else if ($this.attr('type') == 'checkbox') {
            $inputs.prop('checked', $this.prop('checked'));
        } else {
            $inputs.val($this.val());
        }

        propegateDisplayValue($this, $inputs);
    }

    function matchSolutions() {
        var products = [],
            services = [];

        $('[data-tags]').each(function() {
            var $solution = $(this),
                $basketSolution = $(['.configurator-solutions-basket [data-solution-id="', '"]']
                    .join($solution.data('solution-id'))
                ),
                $addMoreSolution = $(['.add-more-modal [data-solution-id="', '"]']
                    .join($solution.data('solution-id'))
                ),
                matched = false,
                tags = $solution.data('tags'),
                categories = $solution.data('categories'),
                isFeatured = $solution.data('featured'),
                solutions = $solution.hasClass('product') ? products : services,
                config = $('form.global').serializeObject();

            // Filter by tags / values
            $.each(tags, function(index, item) {
                for (var prop in config) {
                    matched = matched || config[prop] == item || ($.isArray(config[prop]) && $.inArray(item, config[prop]) !== -1);

                    if (matched) {
                        break;
                    }
                }
            });

            // Filter by categories and featured flag
            if (matched) {
                $.each(categories, function(index, item) {
                    if (isFeatured && $.inArray(item, solutions) == -1) {
                        solutions.push(item);
                    } else {
                        matched = false;
                    }
                });
            }

            $addMoreSolution.find('[data-selected]').attr('data-selected', matched);
            $basketSolution[matched ? 'removeClass' : 'addClass']('hidden');
            $solution.parent()[matched ? 'removeClass' : 'addClass']('hidden');
        });
    }

    $('input[type="number"]').on('change', function(e) {
        var $this = $(this), 
            val = $this.val();

        $this.val(val > 0 ? parseInt(val) : 1);

    });

    $('form.global :input').on('change', function(e) {
        var $this = $(this),
            $inputs = $(['.scoped [data-input-id="', '"]'].join($this.data('input-id'))),
            blockSteps = true,
            name = $this.attr('name'),
            values = $this.val();

        // Propagate value to siblings.
        propegateValue($this, $inputs);
        calculatePrice();

        if ($('[data-step="1"]').hasClass('active')) {
            // Race condition.
            // Timeout to support the selectmenu close menu timeout.
            // setTimeout(function() {
            //     $this
            //         .closest('form')
            //         .find('.form-group')
            //         .not('.hidden')
            //         .find('input, select')
            //         .each(function() {
            //             var $input = $(this);

            //             if ($input.hasClass('selectpicker')) {
            //                 blockSteps = !blockSteps || !$input.selectpicker('val');
            //             } else if ($input.attr('type') !== 'radio' || $input.attr('type') !== 'checkbox') { 
            //                 blockSteps = !blockSteps || !$input.val();
            //             }
            //         });

            //     $('.configurator-steps li, .next-step-btn')
            //         .not('.active, li:first-child')
            //         [blockSteps ? 'addClass' : 'removeClass']('disabled');

            //     // Match solutions
            //     !blockSteps && matchSolutions();
            // }, 500);
            
            if ($.isArray(values)) {
                $.each(values, function() {
                    trackEvent('quote', 'input', [name, this].join(':'), 0);
                });
            } else {
                trackEvent('quote', 'input', [name, values].join(':'), 0);
            }

            matchSolutions();
        } 
        // Growl ?
        // else if (!($this.attr('type') == 'radio' && !$this.prop('checked'))) {
        //     msg = ['<strong>', $this.attr('name'), 'successfully configured to', ['“', '”'].join($this.val()), 'globally!</strong>'].join(' ');
        //     growl(msg, 'info', true);
        // }
    });
    
    matchSolutions();
    calculatePrice();

    $('select[data-related-input-id]')
        .each(function(index, item) {
            var $this = $(this),
                $relatedInput = $(['[data-input-id="', '"]'].join($this.data('related-input-id')));

            $relatedInput.prop('disabled', true);
            $relatedInput.selectpicker('refresh');
        })
        .on('change', function(e) {
            var $this = $(this),
                $selectedOption = $($this.prop('selectedOptions')),
                $relatedInput = $(['[data-input-id="', '"]'].join($this.data('related-input-id')));

            $relatedInput
                .prop('disabled', !$selectedOption.length)
                .selectpicker('refresh')
                .selectpicker('deselectAll')
                .find('option')
                .each(function(index, item) {
                    var isRelevent = !$selectedOption.length || 
                        $(this).data('related-value-id') == $selectedOption.data('value-id');

                    $relatedInput
                        .next()
                        .find(['[data-original-index="', '"]'].join(index))
                        [isRelevent ? 'removeClass' : 'addClass']('hidden');
                });
        });

    $('.configurator-steps li[data-step]').on('click', function(e) {
        var $this = $(this),
            $list = $this.parent(),
            $items = $list.find('li')
            $steps = $items.filter('[data-step]'),
            previousIndex = $steps.filter('.active').index(),
            thisIndex = $this.index(),
            isLast = thisIndex == $steps.length,
            isFirst = thisIndex == 1,
            scrollWidth = $list.get(0).scrollWidth,
            scrollPosition = isFirst ? 0 : isLast ? scrollWidth : (scrollWidth / 2) - ($this.outerWidth() / 2) - 35;

        if ($this.hasClass('disabled') || $this.hasClass('active')) {
            e.stopPropagation();
            e.preventDefault();
            return;
        }

        if (history.pushState) {
            history.pushState(null, null, $this.find('a').attr('href'));
        } else {
            location.hash = $this.find('a').attr('href');
        }

        $('html, body').animate({
            scrollTop: 0
        }, 500);

        $this
            .parent()
            .animate({
                scrollLeft: scrollPosition
            }, 500);

        $items
            .first()
            [isFirst ? 'addClass' : 'removeClass']('disabled')
            .end()
            .last()
            [isLast ? 'addClass' : 'removeClass']('disabled');

        isLast && calculatePriceBuckets();
        isLast && selectSolutions();
        isLast && selectCategories();
        isLast && getSolutionsConfiguration();

        trackEvent('quote', 'step', [previousIndex > -1 ? previousIndex : 0, thisIndex].join(':'), 0);
        _gaq.push(['_trackPageview', location.pathname + location.search + location.hash]);
    });

    $('.next-step-btn, .prev-step-btn').on('click', function(e) {        
        if ($(this).hasClass('disabled')) {
            e.preventDefault();
            e.stopImmediatePropagation();
        } else {
            $('.configurator-steps li[data-step].active')
                [$(this).hasClass('next-step-btn') ? 'next': 'prev']()
                .find('a')
                .click();
        }
    });

    $('.configurator-steps li').not('[data-step]').on('click', function(e) {
        var $this = $(this),
            $items = $this.parent().find('li'),
            activeIndex = $items.filter('.active').index(),
            thisIndex = $this.index(),
            isNext = thisIndex == $items.length - 1,
            nextIndex = isNext ? activeIndex + 1 : activeIndex - 1;

        e.preventDefault();

        if ($this.hasClass('disabled')) {
            e.stopPropagation();
            return;
        }

        if (thisIndex != nextIndex) {
            $items.eq(nextIndex).find('a').click();
        }
    });

    $('.configurator-solutions-wrapper .btn-add-more').on('click', function(e) {
        var $solutions = $(this)
            .closest('.configurator-solutions-wrapper')
            .find('[data-solution-id]');

        $solutions.each(function(index, item) {
            var $solution = $(this);
                $addMoreSolution =  $(['.add-more-modal [data-solution-id="', '"]']
                    .join($solution.data('solution-id'))
                );

            $addMoreSolution.find('[data-selected]').attr('data-selected', !$solution.parent().hasClass('hidden'));
        });

        setTimeout(function() {
            $solutions
                .parent()
                .filter('.expanded')
                .find('a.close-btn')
                .click();
        }, 500);

        refreshCategoryCarousel($solutions.hasClass('product'));
    });

    $('.modal [data-solution-id] .btn-radio').on('click', function(e) {
        e.preventDefault();

        var $this = $(this),
            $related = $this.closest('[data-solution-id]').parent().siblings(),
            selected = $this.attr('data-selected') != 'true',
            productOrService = $this.closest('[data-solution-id]').hasClass('product') ? 'product' : 'service';

        $this
            .attr('data-selected', selected)
            .find('.action-name')
            .text(selected ? gettext('selected') : gettext('select'));

        $related
            .find('[data-selected]')
            .attr('data-selected', false)
            .find('.action-name')
            .text(gettext('select'));
    });

    $('.modal .btn-add-more').on('click', function(e) {
        var className,
            itemNumber = 0,
            $solutions = $(this)
                .closest('.modal')
                .find('[data-solution-id]');

        className = $solutions.hasClass('service') ? '.services' : '.products';

        $(['.configurator-solutions-wrapper ', ' [data-solution-id]'].join(className))
            .map(function(item, index) {
                // To preverve ordering.
                return $solutions.filter(['[data-solution-id="', '"]'].join($(this).data('solution-id')));
            })
            .each(function(index, item) {
                var msg,
                    isAdded = false,
                    isRemoved = false,
                    $solution = $(this),
                    $basketSolution = $(['.configurator-solutions-basket [data-solution-id="', '"]']
                        .join($solution.data('solution-id'))
                    ),
                    $configuratorSolution = $(['.configurator-solutions-wrapper [data-solution-id="', '"]']
                        .join($solution.data('solution-id'))
                    ),
                    selected = $solution
                        .find('[data-selected]')
                        .attr('data-selected') == 'true',
                    solutionName = $solution.find('.face > h4').text();

                isAdded = $basketSolution.hasClass('hidden') && selected;
                isRemoved = !$basketSolution.hasClass('hidden') && !selected;

                $basketSolution[selected ? 'removeClass' : 'addClass']('hidden');

                if (isAdded || isRemoved) {
                    itemNumber++;
                    setTimeout(function() {
                        $configuratorSolution
                            .parent()
                            .css('opacity', selected ? 0 : 1)
                            [selected ? 'removeClass' : 'addClass']('hidden')
                            .animate({'opacity':  selected ? 1 : 0}, {
                                duration: 500,
                                complete: function() {
                                    msg = ['<strong>', solutionName, isAdded ? gettext('added!') : gettext('removed!'), '</strong>'].join(' ');
                                    growl(msg, isAdded ? 'success' : 'danger', true);
                                    showHideEmptyMsg($solutions.hasClass('product'));
                                    trackEvent('quote', isAdded ? 'added' : 'removed', solutionName, 0);
                                }
                            });
                    }, 500 * itemNumber);
                }
            });
    });

    $('.modal .btn-swap').on('click', function(e) {
        var msg,
            $selectedSolution = $(this)
                .closest('.swap-modal')
                .find('.active [data-selected="true"]')
                .closest('[data-solution-id]'),
            $configuratorSolution = $(['.configurator-solutions-wrapper [data-solution-id="', '"]']
                .join($selectedSolution.data('solution-id'))
            ),
            $basketSolution = $(['.configurator-solutions-basket [data-solution-id="', '"]']
                .join($selectedSolution.data('solution-id'))
            ),
            solutionName = $selectedSolution.find('.face > h4').text();

        $('.expanded').find('.remove-btn').click();
        $basketSolution.removeClass('hidden');

        setTimeout(function() {
            $configuratorSolution
                .parent()
                .css('opacity', 0)
                .removeClass('hidden')
                .animate({'opacity': 1}, {
                    duration: 500,
                    complete: function() {
                        showHideEmptyMsg($selectedSolution.hasClass('product'));
                        msg = ['<strong>', solutionName, gettext('added!'), '</strong>'].join(' ');
                        growl(msg, 'success', true);

                        trackEvent('quote', 'added' , solutionName, 0);
                    }
                });
        }, 1500);
    });

    $('.actions a.setup-btn').on('click', function(e) {
        var $solution = $(this).closest('[data-pricing-formula]');
        $solution.prop('$inputCache', $solution.find('input, select, textarea').clone());
    });

    $('.actions a.cancel-btn').on('click', function(e) {
        var $solution = $(this).closest('[data-pricing-formula]');

       $solution.prop('$inputCache').each(function(input, index) {
            var $this = $(this),
                $inputs = $solution.find(['[data-input-id="', '"]'].join($this.data('input-id')));

            propegateValue($this, $inputs);
        });


        
        // $solution.find('a.close-btn').click();
        $solution.toggleClass('configuring');
    });

    $('.actions a.remove-btn').on('click', function(e) {
        var msg,
            $solution = $(this).closest('[data-pricing-formula]'),
            $basketSolution = $(['.configurator-solutions-basket [data-solution-id="', '"]']
                .join($solution.data('solution-id'))
            ),
            solutionName = $solution.find('.face > h4').text();

        $solution.find('a.close-btn').click();
        $basketSolution.addClass('hidden');

        setTimeout(function() {
            $solution
                .parent()
                .animate({
                    'opacity': 0
                },
                {
                    duration: 500,
                    complete: function() {
                        $solution
                            .parent()
                            .addClass('hidden')
                            .css('opacity', 1);

                        showHideEmptyMsg($solution.hasClass('product'));

                        msg = ['<strong>', solutionName, gettext('removed!'), '</strong>'].join(' ');
                        growl(msg, 'danger', true);
                        trackEvent('quote', 'removed' , solutionName, 0);
                    }
                });
        }, 600);
    });

    $('[data-pricing-formula]').each(function(index, item) {
        var $swapBtn = $(this).find('a.swap-btn');
            $tab = $(['#', $swapBtn.data('swap-tab')].join('')),
            isSwappable = $tab.find('[data-solution-id]').length > 1;

        $swapBtn[isSwappable ? 'removeClass' : 'addClass']('disabled');
    });

    $('.actions a.swap-btn').on('click', function(e) {
        if ($(this).hasClass('disabled')) {
            return e.stopImmediatePropagation();
        }

        var $solution = $(this).closest('[data-pricing-formula]'),
            productOrService = $solution.hasClass('product') ? 'products' : 'services',
            $modal = $(['#swap-', '-modal'].join(productOrService)),
            $tab = $modal.find(['#', $(this).data('swap-tab')].join(''))

        $tab
            .find('[data-selected]')
            .attr('data-selected', false)
            .end()
            .find(['[data-solution-id="', '"] [data-selected]']
                .join($solution.data('solution-id'))
            )
            .click()
            .end()
            .siblings()
            .removeClass('active')
            .end()
            .addClass('active');
    });

    $('.configurator-solutions .face').on('click', function(e) {
        $(this).find('a.expand-btn').click();
    });

    $('.configurator-solutions a.expand-btn').on('click', function(e) {
        e.stopImmediatePropagation();

        // Consider isolating in a bound function for recalculating on resize.
        var $column = $(this).parent().parent().parent(),
            origHeight = $column.height(),
            $back = $column.find('.back'),
            $clone = $column.clone().empty().append($column.children()),
            position = $column.position(),
            width = [
                parseFloat($column.css('width')) /
                parseFloat($column.parent().css('width')) * 100, '%'
            ].join('');

        $column
            .css({
                'min-height': origHeight
            })
            .before($clone
                .find('a.close-btn')
                .on('click', function($clone, position, width, e) {
                    $clone
                        .animate({
                            'width': width,
                            'left': position.left
                        },
                        {
                            duration: $(window).width() < 768 ? 1 : 500,
                            start: function() {
                                $clone.removeClass('expanded');
                            },
                            complete: function() {
                                $column
                                    .append($clone.children())
                                    .attr('style', '');
                                $clone.remove();
                            }
                        });
                }.bind(null, $clone, position, width))
                .end()
                .css({
                    'position': 'absolute',
                    'top': position.top,
                    'left': position.left,
                    'width': width,
                    'z-index': '100'
                })
                .animate({
                    'width': '100%',
                    'left': '0'
                },
                {
                    duration: $(window).width() < 768 ? 1 : 500,
                    complete: function() {
                        $clone.addClass('expanded');
                    }
                })
            )
            .siblings('.expanded')
            .find('a.close-btn')
            .click();
    });

    $('[data-max-options]').on('change', function() {
        var $this = $(this),
            values = $this.selectpicker('val'),
            max = $this.data('max-options');

        if (values && values.length == max) {
            setTimeout(function() {
                $this
                    .next()
                    .removeClass('open');

                $this.closest('form').trigger('click');
            }, 100);
        }
    });

    // Not sure if this works anymore.
    $('body').on('click', function(e) {
        var $expanded = $(e.target).parents('.expanded');

        if (!$expanded.length) {
            $(e.target).parents('.expanded').find('a.close-btn').click();
        }
    });

    function validateEmail(email) {
        var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
        return re.test(email);
    }

    function validatePhone(phone) {
        var re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
        return re.test(phone);
    }

    function validateFormInput($this) {
        var isValid = $this.attr('type') == 'email' ? validateEmail($this.val()) : $this.val() != '',
            msg;

        if (!isValid) {
            msg = ['<strong>', '</strong>'].join(interpolate(gettext('%(fieldName)s is not valid!'), {
                fieldName: $this.parent().find(['[for="', '"]'].join($this.attr('name'))).text()
            }, true));
            growl(msg, 'warning', true);
        }

        $this
            .closest('.form-group')
            [isValid ? 'removeClass' : 'addClass']('has-error has-feedback');

        return isValid;
    }

    $('form.scoped :input').not('.btn').on('change blur', function(e) {
        validateFormInput($(this));
    });

    $('.actions a.apply-btn').on('click', function(e) {
        var msg,
            price = 0,
            isValidated = true,
            $solution = $(this).closest('[data-pricing-formula]'),
            $form = $solution.find('form'),
            $basketSolution = $(['.configurator-solutions-basket [data-solution-id="', '"]']
                .join($solution.data('solution-id'))
            ),
            $addMoreSolution = $(['.add-more-modal [data-solution-id="', '"]']
                .join($solution.data('solution-id'))
            ),
            $swapSolution = $(['.swap-modal [data-solution-id="', '"]']
                .join($solution.data('solution-id'))
            ),
            solutionName = $solution.find('.face > h4').text();


        $form.find('.form-group').not('.hidden').find('input, select, textarea').each(function(index, item) {
            var isValid = validateFormInput($(this));
            isValidated = isValidated && isValid;
        });

        if (!isValidated) {
            return e.stopImmediatePropagation();
        }

        if ($solution.find('.apply-global').prop('checked')) {
            $solution.find('input, select, textarea').each(function(index, item) {
                var $this = $(this),
                    $global = $(['.global [data-input-id="', '"]'].join($this.data('input-id')));
                
                propegateValue($this, $global);
    
                if (!($this.attr('type') == 'radio' && !$this.prop('checked'))) {
                    $global.trigger('change');
                }
            });
        } else {
            price = parseFloat(getPrice(String($solution.data('pricing-formula')), 
                $solution.find('form').serializeObject()
            )).toLocaleString();

            $basketSolution
                .find('.price span')
                .text(price);

            $addMoreSolution
                .find('.price span')
                .text(price);

            $swapSolution
                .find('.price span')
                .text(price);

            $solution
                .find('.price span')
                .text(price);

            $solution.find('input, select, textarea').each(function(index, item) {
                var $this = $(this),
                    $inputs = $this.closest('form').find(['[data-input-id="', '"]'].join($this.data('input-id')));
                
                propegateDisplayValue($this, $inputs);
            });
        }

        // $solution.find('a.close-btn').click();
        $solution.toggleClass('configuring');

        msg = ['<strong>', solutionName, gettext('configured!'), '</strong>'].join(' ');
        growl(msg, 'info', true);
        trackEvent('quote', 'configured', solutionName, 0);
    });

    $('.actions a.setup-btn, .actions a.cancel-btn, .actions a.apply-btn').on('click', function(e) {
        var $this = $(this),
            $solution = $this.closest('[data-pricing-formula]').parent();

        $solution
            .find('.form-group')
            .removeClass('has-error has-feedback');

        if (!$this.hasClass('disabled')) {
            $solution.toggleClass('configuring');
        }
    });

    $('form.contact-form :input').not('.btn').on('change blur', function(e) {
        validateFormInput($(this));
    });

    $('.contact-form button').on('click', function(e) {
        var $form = $(this).closest('form'),
            data = $form.serializeObject(),
            isValidated = true,
            msg;

        $form.find('.form-group').not('.hidden').find('[name]').each(function(index, item) {
            var isValid = validateFormInput($(this));
            isValidated = isValidated && isValid;
        });

        isValidated && $.ajax({
            type: 'POST',
            url: '/email/',
            data: data,
            beforeSend: function(request) {
                request.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
            }
        })
        .done(function(response, status, xhr) {
            if (response == '1') {
                $form.get(0).reset();
                msg = ['<strong>', '</strong>'].join(interpolate(gettext('Thanks for reaching out %(fname)s, we\'ll get back to you shortly.'), data, true));
                growl(msg, 'success', true);
                trackEvent('contact', 'sent', 1);

            } else {
                msg = ['<strong>', '</strong>'].join(gettext('We were unable to deliver your message, please try again later.'));
                growl(msg, 'danger', true);
            }
        });
    });

    $('#partner-info-modal form :input').not('.btn').on('change blur', function(e) {
        validateFormInput($(this));
    });

    $('#partner-info-modal .btn-submit-modal').on('click', function(e) {
        var $modal = $(this).closest('.modal'),
            $form = $modal.find('form'),
            data = $form.serializeObject(),
            isValidated = true,
            msg;

        $form.find('.form-group').not('.hidden').find('[name]').each(function(index, item) {
            var isValid = validateFormInput($(this));
            isValidated = isValidated && isValid;
        });

        isValidated && $.ajax({
            type: 'POST',
            url: '/salesforce/',
            data: data,
            traditional: true,
            beforeSend: function(request) {
                request.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
            }
        })
        .done(function(response, status, xhr) {
            if (response == '200') {
                $form.get(0).reset();
                msg = ['<strong>', '</strong>'].join(interpolate(gettext('Thanks for reaching out %(first_name)s, we\'ll get back to you shortly.'), data, true));
                growl(msg, 'success', true);
                $modal.find('.close').click();
                trackEvent('partnership', 'submitted', 1);
            } else {
                msg = ['<strong>', '</strong>'].join(gettext('We were unable to deliver your partnership request, please try again later.'));
                growl(msg, 'danger', true);
            }
        });
    });
    
    $('#partner-info-modal .btn-dismiss-modal').on('click', function(e) {
        trackEvent('partnership', 'canceled', 0);
    });

    $('#user-info-modal form :input').not('.btn').on('change blur', function(e) {
        validateFormInput($(this));
    });

    $('#user-info-modal .btn-submit-modal').on('click', function(e) {
        var $modal = $(this).closest('.modal'),
            $form = $modal .find('form'),
            data = $.extend($form.serializeObject(), $('form.global').serializeObject(true)),
            isValidated = true,
            msg;

        $form.find('.form-group').not('.hidden').find('[name]').each(function(index, item) {
            var isValid = validateFormInput($(this));
            isValidated = isValidated && isValid;
        });

        isValidated && $.ajax({
            type: 'POST',
            url: '/salesforce/',
            data: data,
            traditional: true,
            beforeSend: function(request) {
                request.setRequestHeader('X-CSRFToken', $.cookie('csrftoken'));
            }
        })
        .done(function(response, status, xhr) {
            if (response == '200') {
                $form.get(0).reset();
                msg = ['<strong>', '</strong>'].join(interpolate(gettext('Thanks for reaching out %(first_name)s, we\'ll get back to you shortly.'), data, true));
                growl(msg, 'success', true);
                $modal.find('.close').click();
                trackEvent('quote', 'submitted', 1);
            } else {
                msg = ['<strong>', '</strong>'].join(gettext('We were unable to deliver your quote request, please try again later.'));
                growl(msg, 'danger', true);
            }
        });
    });

    $('#user-info-modal .btn-dismiss-modal').on('click', function(e) {
        trackEvent('quote', 'canceled', 0);
    });

    $(document)
        .one('mouseenter', function(e) {
            $.isTouchOn = false;
            $.isMouseOn = !$.isTouchOn;
            
            $(this).one('touchstart', function(e) {
                $.isTouchOn = true;
                $.isMouseOn = !$.isTouchOn;
            });
        })
        .one('touchstart', function(e) {
            $.isTouchOn = false;
            $.isMouseOn = !$.isTouchOn;
            
            $(this).one('mouseenter', function(e) {
                $.isTouchOn = true;
                $.isMouseOn = !$.isTouchOn;
            });
        });

    $('[data-toggle="tooltip"]')
        .tooltip({
            container: 'body',
            trigger: 'hover',
            placement: function(context, source) {
                return $(source).data('placement');
            }
        })
        .on('show.bs.tooltip', function(e) {
            if ($.isTouchOn) {
                e.preventDefault();
            }
        });


    // (function() {
    //     // Setting a selected property to an option breaks the layout. This is a temporary fix. 
    //     var $configuratorStepNext = $('.configurator-steps li').last();
    //     $configuratorStepNext.css('float', 'initial');
    //     setTimeout(function() {
    //         $configuratorStepNext.css('float', 'right');
    //     }, 0);
    // })();
        
    function onHashChange(e) {
        setTimeout(function() {
            var $link = $(['[href="', '"]'].join(location.hash)).first();

            if (!$link.hasClass('active') && !$link.parent().hasClass('active')) {
                $link.trigger('click');
            }
        }, 50);
    }

    window.addEventListener('hashchange', onHashChange);

    location.hash && onHashChange();

    if ($('.configurator-steps').length > 0) {
        window.onbeforeunload = function(e) {
            var message = gettext('You have unsaved changes.');

            e = e || window.event;
            e.returnValue = message;

            return message;
        }; 
    }
});
