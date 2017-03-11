<?php
namespace NethServer\Module;


use Nethgui\System\PlatformInterface as Validate;

/**
 * settings of the stephdl Repository
 * 
 * @author stephane de Labrusse <stephdl@de-labrusse.fr>
 */
class Stephdl extends \Nethgui\Controller\AbstractController
{

    protected function initializeAttributes(\Nethgui\Module\ModuleAttributesInterface $base)
    {
        return \Nethgui\Module\SimpleModuleAttributesProvider::extendModuleAttributes($base, 'Configuration', 6);
    }

    public function initialize()
    {
        parent::initialize();
        $this->declareParameter('login', Validate::ANYTHING, array('configuration', 'stephdl', 'login'));
        $this->declareParameter('password', Validate::ANYTHING, array('configuration', 'stephdl', 'password'));
    }

    private function readuuid()
    {
        $uuid = $this->getPlatform()->exec('sudo dmidecode -s system-uuid')->getOutput();
        return $uuid;
    }
    public function bind(\Nethgui\Controller\RequestInterface $request)
    {
        parent::bind($request);
        $this->uuid = $this->readuuid();
    }
 
    protected function onParametersSaved($changedParameters)
    {
        parent::onParametersSaved($changedParameters);
        $this->getPlatform()->signalEvent('nethserver-stephdl-update');
    }

    public function prepareView(\Nethgui\View\ViewInterface $view)
    {
        parent::prepareView($view);

        if (!$this->uuid) {
            $this->uuid = $this->readuuid();
        }
        $view['uuid'] = $this->uuid;
    }


}
