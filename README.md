# book_website

https://github.com/BlackrockDigital/startbootstrap-shop-homepage

general sources: 
https://riptutorial.com/django/example/32472/use-of----extends---------include----and----blocks---
https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/

src="{{ url_for('static', filename='assets/img/pink.jpg')}}" alt=""

.plant-filters {
    margin: 1.125rem -3rem 0;
    background-color: #f8f8f7;
    padding: 1.25rem 3rem;
}

.filter-text {
    display: inline-block;
    vertical-align: middle;
    margin-right: 2rem;
    font-size: .8125rem;
    line-height: 1.8;
}

.filter-options {
    display: inline-block;
    background-color: #f8f8f7;
    vertical-align: middle;
}

.option-title {
    
}

<!-- FORM-->
<div class="grid-x grid-padding-x"><div class="cell">
    <form class="plant-filters">
      <h5 class="filter-text">Filter By</h5>
<ul class="filter-options" id="filter-tabs" data-tabs="b9433d-tabs" data-active-collapse="true" role="tablist"><li class="option-title is-active" role="presentation">
        <a href="#filter_options_1" aria-selected="true" role="tab" aria-controls="filter_options_1" id="filter_options_1-label" tabindex="0">
          Features <svg width="12" height="8" fill="none" xmlns="http://www.w3.org/2000/svg" class=""><title>Show features filters</title><path d="M1 1l5 5 5-5" stroke="#2D2A24" stroke-width="1.5"></path></svg></a>
      </li><li class="tabs-title" role="presentation">
        <a href="#filter_options_2" role="tab" aria-controls="filter_options_2" aria-selected="false" id="filter_options_2-label" tabindex="-1">
          Variety <svg width="12" height="8" fill="none" xmlns="http://www.w3.org/2000/svg" class=""><title>Show variety filters</title><path d="M1 1l5 5 5-5" stroke="#2D2A24" stroke-width="1.5"></path></svg></a>
      </li><li class="tabs-title" role="presentation">
        <a href="#filter_options_3" role="tab" aria-controls="filter_options_3" aria-selected="false" id="filter_options_3-label" tabindex="-1">
          Size <svg width="12" height="8" fill="none" xmlns="http://www.w3.org/2000/svg" class=""><title>Show size filters</title><path d="M1 1l5 5 5-5" stroke="#2D2A24" stroke-width="1.5"></path></svg></a>
      </li></ul>
<button type="reset" class="button clear clear-filters show-for-medium">Clear All Filters</button><div class="tabs-content" data-tabs-content="filter-tabs"><div class="tabs-panel  is-active" id="filter_options_1" role="tabpanel" aria-labelledby="filter_options_1-label">
        <fieldset data-filter-group=""><div class="options-container has-title"><h6 class="options-title">Style</h6><label for="features_filter_options_1_style_blooming">
                    <input type="checkbox" id="features_filter_options_1_style_blooming" value=".blooming"><span> Blooming</span>
                  </label><label for="features_filter_options_1_style_patterned">
                    <input type="checkbox" id="features_filter_options_1_style_patterned" value=".patterned"><span> Patterned</span>
                  </label><label for="features_filter_options_1_style_trending">
                    <input type="checkbox" id="features_filter_options_1_style_trending" value=".trending"><span>Trending</span>
                  </label><label for="features_filter_options_1_style_cascading">
                    <input type="checkbox" id="features_filter_options_1_style_cascading" value=".cascading"><span>Cascading</span>
                  </label></div><div class="options-container has-title"><h6 class="options-title">Light</h6><label for="features_filter_options_1_light_low-light">
                    <input type="checkbox" id="features_filter_options_1_light_low-light" value=".low-light"><span>Low Light</span>
                  </label><label for="features_filter_options_1_light_bright-light">
                    <input type="checkbox" id="features_filter_options_1_light_bright-light" value=".bright-light"><span> Bright Light</span>
                  </label></div><div class="options-container has-title"><h6 class="options-title">Benefit</h6><label for="features_filter_options_1_benefit_pet-friendly">
                    <input type="checkbox" id="features_filter_options_1_benefit_pet-friendly" value=".pet-friendly"><span> Pet Friendly</span>
                  </label><label for="features_filter_options_1_benefit_air-purifying">
                    <input type="checkbox" id="features_filter_options_1_benefit_air-purifying" value=".air-purifying"><span>Air Purifying</span>
                  </label></div></fieldset></div><div class="tabs-panel " id="filter_options_2" role="tabpanel" aria-labelledby="filter_options_2-label" aria-hidden="true">
        <fieldset data-filter-group=""><div class="options-container"><label for="variety_filter_options_2__air-plant">
                    <input type="checkbox" id="variety_filter_options_2__air-plant" value=".air-plant"><div class="filter pcp_filter_icon_air-plant"></div><span>Air Plant</span>
                  </label><label for="variety_filter_options_2__calathea">
                    <input type="checkbox" id="variety_filter_options_2__calathea" value=".calathea"><div class="filter pcp_filter_icon_calathea"></div><span> Calathea</span>
                  </label><label for="variety_filter_options_2__fern">
                    <input type="checkbox" id="variety_filter_options_2__fern" value=".fern"><div class="filter pcp_filter_icon_fern"></div><span> Fern</span>
                  </label><label for="variety_filter_options_2__fiddle-leaf-fig">
                    <input type="checkbox" id="variety_filter_options_2__fiddle-leaf-fig" value=".fiddle-leaf-fig"><div class="filter pcp_filter_icon_fiddle-leaf-fig"></div><span> Fiddle Leaf Fig</span>
                  </label><label for="variety_filter_options_2__marimo">
                    <input type="checkbox" id="variety_filter_options_2__marimo" value=".marimo"><div class="filter pcp_filter_icon_marimo"></div><span> Marimo</span>
                  </label><label for="variety_filter_options_2__monstera">
                    <input type="checkbox" id="variety_filter_options_2__monstera" value=".monstera"><div class="filter pcp_filter_icon_monstera"></div><span> Monstera</span>
                  </label><label for="variety_filter_options_2__money-tree">
                    <input type="checkbox" id="variety_filter_options_2__money-tree" value=".money-tree"><div class="filter pcp_filter_icon_money-tree"></div><span> Money Tree</span>
                  </label><label for="variety_filter_options_2__parlor-palm">
                    <input type="checkbox" id="variety_filter_options_2__parlor-palm" value=".parlor-palm"><div class="filter pcp_filter_icon_parlor-palm"></div><span> Parlor Palm</span>
                  </label><label for="variety_filter_options_2__peperomia">
                    <input type="checkbox" id="variety_filter_options_2__peperomia" value=".peperomia"><div class="filter pcp_filter_icon_peperomia"></div><span> Peperomia</span>
                  </label><label for="variety_filter_options_2__philodendron">
                    <input type="checkbox" id="variety_filter_options_2__philodendron" value=".philodendron"><div class="filter pcp_filter_icon_philodendron"></div><span> Philodendron</span>
                  </label><label for="variety_filter_options_2__pilea">
                    <input type="checkbox" id="variety_filter_options_2__pilea" value=".pilea"><div class="filter pcp_filter_icon_pilea"></div><span> Pilea</span>
                  </label><label for="variety_filter_options_2__pothos">
                    <input type="checkbox" id="variety_filter_options_2__pothos" value=".pothos"><div class="filter pcp_filter_icon_pothos"></div><span> Pothos</span>
                  </label><label for="variety_filter_options_2__snake-plant">
                    <input type="checkbox" id="variety_filter_options_2__snake-plant" value=".snake-plant"><div class="filter pcp_filter_icon_snake-plant"></div><span> Snake Plant</span>
                  </label><label for="variety_filter_options_2__succulent">
                    <input type="checkbox" id="variety_filter_options_2__succulent" value=".succulent"><div class="filter pcp_filter_icon_succulent"></div><span> Succulent</span>
                  </label><label for="variety_filter_options_2__zz">
                    <input type="checkbox" id="variety_filter_options_2__zz" value=".zz"><div class="filter pcp_filter_icon_zz"></div><span> ZZ</span>
                  </label></div></fieldset></div><div class="tabs-panel " id="filter_options_3" role="tabpanel" aria-labelledby="filter_options_3-label" aria-hidden="true">
        <fieldset data-filter-group=""><div class="options-container"><label for="size_filter_options_3__mini-2-5">
                    <input type="checkbox" id="size_filter_options_3__mini-2-5" value=".mini-2-5"><div class="filter pcp_filter_icon_mini-2-5"></div><span>Mini 2.5"</span>
                  </label><label for="size_filter_options_3__x-small-4">
                    <input type="checkbox" id="size_filter_options_3__x-small-4" value=".x-small-mixitup-4"><div class="filter pcp_filter_icon_x-small-4"></div><span>X-Small 4"</span>
                  </label><label for="size_filter_options_3__small-5">
                    <input type="checkbox" id="size_filter_options_3__small-5" value=".small-mixitup-5"><div class="filter pcp_filter_icon_small-5"></div><span>Small 5"</span>
                  </label><label for="size_filter_options_3__medium-7">
                    <input type="checkbox" id="size_filter_options_3__medium-7" value=".medium-mixitup-7"><div class="filter pcp_filter_icon_medium-7"></div><span>Medium 7"</span>
                  </label><label for="size_filter_options_3__large-12-nyc-only">
                    <input type="checkbox" id="size_filter_options_3__large-12-nyc-only" value=".large-mixitup-12-nyc-only"><div class="filter pcp_filter_icon_large-12-nyc-only"></div><span>Large 12" (NYC Only)</span>
                  </label></div></fieldset><div class="filter-details">
            Measurement is the approximate top diameter of the planter.
          </div></div></div>
    </form>
  </div><div class="cell small-5 medium-6">
  <div class="results-title">
    (<span class="results-count">71 Results</span>)
  </div>
</div>
<div class="cell text-right small-7 hide-for-medium"><a href="https://www.thesill.com/collections/live-plants" class="button clear clear-filters-mobile">Clear All Filters</a></div>
<div class="cell medium-6 medium-text-right">
  <select class="sort-options">
    <option value="manual" selected="selected" disabled="">Sort Options</option>
    <option value="best-selling">Most Popular</option>
    <option value="created-descending">Newest First</option>
    <option value="price-ascending">$ Low to High</option>
    <option value="price-descending">$ High to Low</option>
    <option value="title-ascending">A-Z</option>
    <option value="title-descending">Z-A</option>
  </select>
</div></div>



