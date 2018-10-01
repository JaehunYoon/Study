<?php
/**
 * Created by PhpStorm.
 * User: dsm2017
 * Date: 2018-10-01
 * Time: 오전 8:57
 */

class Entree
{
    public $name;
    public $ingredients = array(); /* ingredient (명) 재료, 구성 요소 */

    public function hasIngredient($ingredient)
    {
        return in_array($ingredient, $this->ingredients);
    }
}