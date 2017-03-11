<?php
namespace NethServer\Module\Dashboard\SystemStatus;

/*
 * Stephane de Labrusse <stephdl@de-labrusse.fr>
 *
 * This script is part of NethServer.
 *
 * NethServer is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * NethServer is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with NethServer.  If not, see <http://www.gnu.org/licenses/>.
 */

class Stephdl extends \Nethgui\Controller\AbstractController
{

    public $sortId = 60;
 
    private $phonehome = "";


    private function readPhoneHome()
    {
        $phonehome = $this->getPlatform()->getDatabase('configuration')->getProp('phone-home', 'uuid');
        return $phonehome;
    }

    public function process()
    {
        $this->phonehome = $this->readPhoneHome();
    }
 
    public function prepareView(\Nethgui\View\ViewInterface $view)
    {

        if (!$this->phonehome) {
            $this->phonehome = $this->readPhoneHome();
        }
        $view['PhoneHome'] = $this->phonehome;

    }
}
