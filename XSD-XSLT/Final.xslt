<?xml version='1.0' encoding='UTF-8'?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:multimap="http://sap.com/xi/XI/SplitAndMerge" version="1.0">
  <xsl:template match="/">
    <EmpMovement>
      <xsl:for-each select="//MovemnetInfo">
        <MovemnetInfo>
          <p_empid>
            <xsl:value-of select="p_empid"/>
          </p_empid>
          <p_perfdate>
            <xsl:value-of select="p_perfdate"/>
          </p_perfdate>
          <p_reason>
            <xsl:value-of select="p_reason"/>
          </p_reason>
          <p_comp>
            <xsl:value-of select="p_comp"/>
          </p_comp>
          <p_div>
            <xsl:value-of select="p_div"/>
          </p_div>
          <p_section>
            <xsl:value-of select="p_section"/>
          </p_section>
          <p_location>
            <xsl:value-of select="p_location"/>
          </p_location>
          <p_dept>
            <xsl:value-of select="p_dept"/>
          </p_dept>
          <p_stagrade>
            <xsl:value-of select="p_stagrade"/>
          </p_stagrade>
          <p_jobcode>
            <xsl:value-of select="p_jobcode"/>
          </p_jobcode>
          <p_basecur1>
            <xsl:value-of select="p_basecur1"/>
          </p_basecur1>
          <p_salary>
            <xsl:value-of select="p_salary"/>
          </p_salary>
          <p_averhrs>
            <xsl:value-of select="p_averhrs"/>
          </p_averhrs>
          <p_hrrate>
            <xsl:value-of select="p_hrrate"/>
          </p_hrrate>
          <p_costp>
            <xsl:value-of select="p_costp"/>
          </p_costp>
          <p_costcen>
            <xsl:value-of select="p_costcen"/>
          </p_costcen>
        </MovemnetInfo>
      </xsl:for-each>
    </EmpMovement>
  </xsl:template>
</xsl:stylesheet>
